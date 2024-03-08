from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsDynamodbTableItem(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    key: str
    table_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_dynamodb_table_item")
    expression_attribute_names: Optional[Dict[str, str]] = None
    projection_expression: Optional[str] = None
