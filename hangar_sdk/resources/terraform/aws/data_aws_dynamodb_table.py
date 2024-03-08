from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class ServerSideEncryption(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="server_side_encryption")


@define(kw_only=True, slots=False)
class DataAwsDynamodbTable(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_dynamodb_table")
    server_side_encryption: Optional[Sequence[ServerSideEncryption]] = None
    tags: Optional[Dict[str, str]] = None
