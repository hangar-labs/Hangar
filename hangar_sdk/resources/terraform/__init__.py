import typing
from typing import Any, Dict, List, Optional, Union, cast

import attrs
from attrs import define, field

from hangar_sdk.core import IGroup, IResource


def indent(string, level):
    result = ""
    lines = string.splitlines()
    if len(lines) == 1:
        return lines[0]
    result += lines[0] + "\n"
    for line in lines[1:-1]:
        result += "    " * level + line + "\n"
    result += "    " * level + lines[-1]
    return result


@define(slots=False)
class Expression:
    expression: str

    def __str__(self) -> str:
        return self.expression

    def __getitem__(self, item):
        return self.expression + f".{item}"

    def __setitem__(self, item, value):
        return self.expression + f".{item} = {value}"

    def __delitem__(self, item):
        return self.expression + f".{item}"


# TODO : FIX
def dict_to_hcl(input_dict, indent=0):
    """
    Convert a nested Python dictionary to a string formatted in HCL.

    :param input_dict: The Python dictionary to convert.
    :param indent: Current indentation level for formatting.
    :return: A string formatted as HCL.
    """

    """
    HCL Example:
    resource "aws_instance" "example" {
        ami           = "ami-0c55b159cbfafe1f0"
        instance_type = "t2.micro"
    }

    Dict Example:
    {
        "resource": {
            "aws_instance": {
                "example": {
                    "ami": "ami-0c55b159cbfafe1f0",
                    "instance_type": "t2.micro"
                }
            }
        },
        "o

    }
    """

    hcl_str = ""
    indent_str = "    " * indent

    for key, value in input_dict.items():
        if isinstance(value, dict):
            hcl_str += (
                f"{indent_str}{key} "
                + "{\n"
                + dict_to_hcl(value, indent + 1)
                + f"{indent_str}"
                + "}\n"
            )
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    hcl_str += (
                        f"{indent_str}{key} "
                        + "{\n"
                        + dict_to_hcl(item, indent + 1)
                        + f"{indent_str}"
                        + "}\n"
                    )
                else:
                    hcl_str += f"{indent_str}{key} = {item}\n"
        else:
            hcl_str += f'{indent_str}{key} = "{value}"\n'

    return hcl_str


def outputValue(value):
    if isinstance(value, str):
        return f'"{value}"'

    elif isinstance(value, bool):
        return "true" if value else "false"

    elif isinstance(value, int):
        return str(value)

    elif isinstance(value, float):
        return str(value)

    elif isinstance(value, list) or isinstance(value, set):
        contents = ",".join([outputValue(e).__str__() for e in value])
        return f"[{contents}]"

    elif isinstance(value, dict):
        contents = "\n".join(
            [f"    {k} = {outputValue(v)}" for k, v in value.items() if v is not None]
        )

        return f"{{\n{contents}\n}}"

    elif isinstance(value, Expression):
        return value.__str__()

    elif isinstance(value, AbstractTerraformBlock):
        return value.__str__()

    else:
        raise ValueError(value.__str__())
        return '"oh no"'


@define(kw_only=True, slots=False)
class AbstractTerraformBlock(IResource):
    _block_type = "block"
    _name: str = field(alias="_name")
    _group: IGroup

    @property
    def group(self) -> IGroup:
        return self._group

    def get_state(self) -> Optional[Dict]:
        return self.group.get_state_manager().get_state(self._top_name)

    def get_type(self) -> str:
        return self._name

    def set_state(self, state):
        self.state = state

    def __str__(self, level=0):
        hcl_string = "{\n"
        for name, afield in self.__dict__.items():
            if afield is not None and not name.startswith("_"):
                if hasattr(afield, "_block_type"):
                    hcl_string += ("    " * level) + afield.__str__(level + 1)
                    continue
                if (
                    isinstance(afield, list)
                    and len(afield) > 0
                    and hasattr(afield[0], "_block_type")
                ):
                    for f in afield:
                        hcl_string += f.__str__(level + 1)
                    continue
                hcl_string += (
                    ("    " * level)
                    + " " * 4
                    + f"{name} = {indent(outputValue(afield),level+1)}\n"
                )
        hcl_string += ("    " * level) + "}"
        if self.__class__._block_type == "resource":
            hcl_string = f"""resource "{self._name}" "{self._top_name}" {hcl_string}"""
        elif self.__class__._block_type == "datasource":
            hcl_string = f"""data "{self._name}" "{self._top_name}" {hcl_string}"""
        elif self.__class__._block_type == "variable":
            hcl_string = f"variable {self._name} {hcl_string}"
        elif self.__class__._block_type == "output":
            hcl_string = f"output {self._top_name} {hcl_string}"
        elif self.__class__._block_type == "module":
            hcl_string = f"module {self._name} {hcl_string}"
        elif self.__class__._block_type == "provider":
            hcl_string = f"provider {self._name} {hcl_string}"
        elif self.__class__._block_type == "terraform":
            hcl_string = f"terraform {self._name} {hcl_string}"
        elif self.__class__._block_type == "block":
            hcl_string = f"{self._name} {hcl_string}"
        hcl_string = ("    " * level) + hcl_string
        return hcl_string + "\n"

    def __getattr__(self, attr: str) -> Any:
        if attr.startswith("_"):
            raise AttributeError(attr)
        else:
            if self.__dict__.get(attr) is not None:
                if self.__getattribute__(attr):
                    return self.__getattribute__(attr)
            if self._block_type == "resource":
                return self._name + "." + self._top_name + "." + attr

            elif self._block_type == "data_source":
                return "data." + self._name + "." + self._top_name + "." + attr

            else:
                return self._name + "." + attr

    def resolve(self):
        return str(self)

    def get_name(self):
        return self._top_name


@define(kw_only=True, slots=False)
class TerraformBlock(AbstractTerraformBlock):
    _block_type = "block"
    _name = ""

    def __post_init__(self, resource_type, **kwargs):
        self.__class__._name = resource_type
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class AbstractTerraformResource(AbstractTerraformBlock):
    _block_type = "resource"
    _name = ""
    _top_name: str = field(alias="_top_name")
    _group: IGroup = field(alias="_group")

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    @typing.no_type_check
    def ref(self):
        return TerraformProxy(self)


@define(slots=False)
class TerraformProxy:
    instance: AbstractTerraformBlock
    attr_path: list = field(default=attrs.Factory(list))

    def __getattr__(self, attr) -> Union[str, "TerraformProxy"]:
        new_path = self.attr_path + [attr]
        attr_value = getattr(self.instance, attr, None)
        if isinstance(attr_value, (AbstractTerraformBlock, list)):
            return TerraformProxy(self.instance.__getattribute__(attr), new_path)

        return cast(str, self.get_hcl_reference(new_path))

    def __getitem__(self, item):
        return TerraformProxy(self.instance, self.attr_path + [f"{item}"])

    def __setitem__(self, item, value):
        return TerraformProxy(self.instance, self.attr_path + [f"{item}"])

    def __delitem__(self, item):
        return TerraformProxy(self.instance, self.attr_path + [f"{item}"])

    def get_hcl_reference(self, attr_path):
        hcl_reference = ""
        if self.instance._block_type == "datasource":
            hcl_reference = "data."

        if "_top_name" in self.instance.__dict__:
            hcl_reference += f"{self.instance._name}.{self.instance._top_name}"
        else:
            hcl_reference += f"{(self.instance._name)}"
        for attr in attr_path:
            hcl_reference += f".{attr}"

        return Expression(hcl_reference)


@define(kw_only=True, slots=False)
class TerraformResource(AbstractTerraformResource):

    def __post_init__(self, resource_type, **kwargs):
        self._block_type = "resource"
        self._name = resource_type
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class AbstractTerraformDatasource(AbstractTerraformBlock):
    _block_type = "datasource"
    _name = ""
    _top_name: str = field(alias="_top_name")
    _group: IGroup = field(alias="_group")

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def ref(self):
        return TerraformProxy(self)


@define(kw_only=True, slots=False)
class TerraformDatasource(AbstractTerraformDatasource):
    _block_type: str = "datasource"

    def __post_init__(self, data_source_type, top_name, **kwargs):
        self._name = data_source_type
        self._top_name = top_name
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class TerraformVariable(AbstractTerraformBlock):
    _block_type = "variable"
    _name = ""
    _top_name = ""

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class TerraformOutput(AbstractTerraformBlock):
    _block_type = "output"
    _name = ""
    _top_name = ""

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class AbstractTerraformProvider(AbstractTerraformBlock):
    _block_type = "provider"
    _name = ""
    _top_name = ""

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class TerraformProvider(AbstractTerraformProvider):
    _block_type = "provider"
    _name = ""

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class TerraformTerraform(AbstractTerraformBlock):
    _block_type = "terraform"
    _name = ""
    _top_name = ""

    def __post_init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)


@define(kw_only=True, slots=False)
class HCLBlockBuilder:
    block_type: str
    labels: List[str]
    kv_pairs: Dict[str, Any]
    nested_blocks: List["HCLBlockBuilder"]

    def __post_init__(self):
        self._top_name = self.block_type + "_" + "_".join(self.labels)

    def __str__(self) -> str:
        hcl_string = ""
        if self.labels:
            hcl_string += f"{self.block_type} "
            for label in self.labels:
                hcl_string += f'"{label}" '
        else:
            hcl_string += f"{self.block_type}"
        hcl_string += "{\n"
        for k, v in self.kv_pairs.items():
            hcl_string += f"    {k} = {outputValue(v)}\n"
        for block in self.nested_blocks:
            hcl_string += block.__str__() + "\n"
        hcl_string += "}"
        return hcl_string

    def add_label(self, label):
        self.labels.append(label)
        return self

    def add_kv_pair(self, k, v):
        self.kv_pairs[k] = v
        return self

    def add_nested_block(self, block):
        self.nested_blocks.append(block)
        return self


@define(kw_only=True, slots=False)
class TerraformModuleCaller:
    _block_type = "module"
    _name = ""
    _top_name = ""
    source: str
    version: str
    input_vars: dict

    def __post_init__(self, name, **kwargs):
        self._name = name
        self.input_vars = kwargs

    def __str__(self) -> str:
        return HCLBlockBuilder(
            block_type="module",
            labels=[self._name],
            kv_pairs={
                "source": self.source,
                "version": self.version,
                **self.input_vars,
            },
            nested_blocks=[],
        ).__str__()
