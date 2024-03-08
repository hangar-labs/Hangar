from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSsmDocument(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ssm_document")
    document_format: Optional[str] = None
    document_version: Optional[str] = None
