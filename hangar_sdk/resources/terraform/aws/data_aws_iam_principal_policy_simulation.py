from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Context(AbstractTerraformBlock):
    key: str
    type: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="context")


@define(kw_only=True, slots=False)
class DataAwsIamPrincipalPolicySimulation(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    action_names: Sequence[str]
    policy_source_arn: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_principal_policy_simulation")
    additional_policies_json: Optional[Sequence[str]] = None
    caller_arn: Optional[str] = None
    context: Optional[Sequence[Context]] = None
    permissions_boundary_policies_json: Optional[Sequence[str]] = None
    resource_arns: Optional[Sequence[str]] = None
    resource_handling_option: Optional[str] = None
    resource_owner_account_id: Optional[str] = None
    resource_policy_json: Optional[str] = None
