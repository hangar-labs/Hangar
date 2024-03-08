from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsEcsService(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    cluster_arn: str
    service_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ecs_service")
    tags: Optional[Dict[str, str]] = None
