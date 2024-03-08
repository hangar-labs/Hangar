from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamSamlProvider(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    saml_metadata_document: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_saml_provider")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
