from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamServerCertificate(AbstractTerraformResource):
    _group: Any
    _top_name: str
    certificate_body: str
    private_key: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_server_certificate")
    certificate_chain: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    path: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
