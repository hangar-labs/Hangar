from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSsmincidentsResponsePlan(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    arn: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ssmincidents_response_plan")
    tags: Optional[Dict[str, str]] = None
