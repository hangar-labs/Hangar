from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AttachmentsSource(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="attachments_source")
    name: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSsmDocument(AbstractTerraformResource):
    _group: Any
    _top_name: str
    content: str
    document_type: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_document")
    attachments_source: Optional[Sequence[AttachmentsSource]] = None
    document_format: Optional[str] = None
    permissions: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    target_type: Optional[str] = None
    version_name: Optional[str] = None
