from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDynamodbTableItem(AbstractTerraformResource):
    _group: Any
    _top_name: str
    hash_key: str
    item: str
    table_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dynamodb_table_item")
    range_key: Optional[str] = None
