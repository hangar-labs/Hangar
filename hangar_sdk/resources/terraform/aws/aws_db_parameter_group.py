from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Parameter(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="parameter")
    apply_method: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbParameterGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    family: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_parameter_group")
    description: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    parameter: Optional[Sequence[Parameter]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
