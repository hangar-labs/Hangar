from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRoute53Zone(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_route53_zone")
    name: Optional[str] = None
    private_zone: Optional[bool] = None
    resource_record_set_count: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    vpc_id: Optional[str] = None
    zone_id: Optional[str] = None
