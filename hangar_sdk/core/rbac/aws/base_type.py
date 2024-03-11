import json
import os
from typing import (Dict, Generic, List, Literal, Set, TypeVar,
                    Union, get_args)

from hangar_sdk.core.rbac.aws.service_roles import ServicePrincipalType

from hangar_sdk.resources.terraform import AbstractTerraformResource

UserArnType = str
EffectType = Union[Literal["Allow"], Literal["Deny"]]

privilege_t = TypeVar("privilege_t")
condition_t = TypeVar("condition_t")


class GenericResourceType(Generic[privilege_t, condition_t]):
    arns: List = []
    actions: List = []
    conditions: List = []
    servicePrincipals: List = []
    principals: Union[List[ServicePrincipalType], Literal["*"]] = []
    statement: Dict = {}

    def __init__(
        self,
        policy=None,
        arns: List = [],
        resources: List[AbstractTerraformResource] = None,
    ):
        self.policy = policy
        self.arns = arns
        if resources is not None:
            self.arns += [
                "${" + str(resource.ref().arn) + "}" for resource in resources
            ]

    def withActions(self, actions: List[privilege_t]):
        self.actions += actions
        return self

    def withCondition(self, identifier: condition_t, condition: Dict = {}):
        self.conditions.append({identifier: condition})
        return self

    def withPrincipals(
        self, principals: Union[List[ServicePrincipalType], Literal["*"]]
    ):
        if principals == "*":
            self.principals = "*"
        else:
            for principal in principals:
                if principal in [
                    get_args(x)[0] for x in get_args(ServicePrincipalType)
                ]:
                    self.servicePrincipals.append(principal)
                else:
                    self.principals.append(principal)

        return self

    def generate_principal_statement(self, effect: EffectType):
        p = []

        if self.principals == "*":
            p = self.principals
        else:
            p = {"Service": self.servicePrincipals, "AWS": self.principals}

        if effect == "Allow":
            return {
                "Principal": p,
            }
        elif effect == "Deny":
            return {
                "NotPrincipal": p,
            }

    def statement(self, effect: EffectType):
        statement = {
            **(self.generate_principal_statement(effect=effect)),
        }

        if len(self.arns) > 0:
            statement["Resource"] = self.arns

            if len(self.actions) > 0:
                statement["Action"] = self.actions

            if len(self.conditions) > 0:
                statement["Condition"] = self.conditions

            return statement
        else:
            raise Exception(
                "Invalid IAM statement: No resources associated with statment"
            )

    def build(self):
        return self.policy.build()


class Policy:
    _policy: Dict[str, List[Dict[str, str]]]
    allowList: List[GenericResourceType] = []
    denyList: List[GenericResourceType] = []

    def __init__(self, version: Literal["2012-10-17"] = "2012-10-17"):
        self._policy: Dict[str, List[Dict[str, str]]] = {
            "Version": version,
            "Statement": [],
        }
        self.resources = []

    def allows(self, resources: Union[GenericResourceType, List[GenericResourceType]]):
        if isinstance(resources, List):
            self.allowList += resources
        else:
            self.allowList.append(resources)

    def denies(self, resources: Union[GenericResourceType, List[GenericResourceType]]):
        if isinstance(resources, List):
            self.denyList += resources
        else:
            self.denyList.append(resources)

    def build(self):
        statements = []

        print(self.allowList)

        for resource in self.allowList:
            resource_statement = resource.statement(effect="Allow")
            statements.append({**resource_statement})

        for resource in self.denyList:
            resource_statement = resource.statement(effect="Deny")
            statements.append({**resource_statement})

        self._policy["Statement"] = statements

        return self

    @property
    def policy(self):
        self.build()

        return self._policy

    @property
    def escaped_json_policy(self):
        return json.dumps(json.dumps(self.policy))[1:-1]


def get_operator_code(name):
    return f"""
    def {name}(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> {name}Statement:
        return {name}Statement(policy=self.policy, arns=arns, resources=resources)
"""


def get_statement_import_code(name):
    return f"""from hangar_sdk.core.rbac.aws.iam_types.{name} import {name}Statement"""


def get_statement_class_code(imports: List, operators: List):
    ops = "\n".join(operators)
    imps = "\n".join(imports)

    return f"""{imps}
from typing import List
from hangar_sdk.core.rbac.aws.base_type import Policy
from hangar_sdk.resources.terraform import AbstractTerraformResource

class Statement():

    def __init__(self, policy: Policy):
        self.policy = policy
    
    {ops}
"""


def generate_types(infile: str, outdirname: str):
    # Create the output directory if it doesn't exist
    os.makedirs(outdirname, exist_ok=True)

    # Read the JSON file
    with open(infile, "r") as j:
        iam = json.load(j)

    statementOperators = []
    statementImports = []

    # Iterate through the JSON data
    for k, v in iam.items():
        name = "aws_" + k.replace("/", "_").replace(
            "-", "_"
        )  # Replace slashes with underscores for valid Python class names
        privileges = set()
        conditions = set()

        print(name)

        if "privileges" in v:
            # Process each privilege and its conditions
            for privilege, details in v["privileges"].items():
                resource_types = details["resource_types"]
                privileges.add(privilege)

                for resource_type in resource_types.values():
                    if "condition_keys" in resource_type:
                        conditions.update(resource_type["condition_keys"])

        # Generate the class code
        class_code = generate_class_code(name, privileges, conditions)
        statementOperators.append(get_operator_code(name))
        statementImports.append(get_statement_import_code(name))

        # Write the class code to a file
        with open(os.path.join(outdirname, f"{name}.py"), "w") as file:
            file.write(class_code)

    with open(os.path.join(os.getcwd(), "statement.py"), "w") as f:
        f.write(
            get_statement_class_code(
                imports=statementImports, operators=statementOperators
            )
        )


def generate_class_code(name, privileges: Set[str], conditions: Set[str]):
    privileges_union = generate_union_type(privileges)
    conditions_union = generate_union_type(conditions)

    class_code = f"""from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

{name}_privilege_type = {privileges_union}
{name}_condition_type = {conditions_union}

class {name}Statement(GenericResourceType[{name}_privilege_type, {name}_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    """

    return class_code


def generate_union_type(items: Set[str]) -> str:
    if not items:
        return "None"
    literals = ", ".join(f'Literal["{item}"]' for item in items)
    return f"Union[{literals}]"


# Example usage
if __name__ == "__main__":
    generate_types("iam-definition.json", "./iam_types")
