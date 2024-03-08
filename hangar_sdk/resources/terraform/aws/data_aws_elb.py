from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsElb(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_elb")
    tags: Optional[Dict[str, str]] = None
