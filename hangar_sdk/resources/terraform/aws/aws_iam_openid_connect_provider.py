from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamOpenidConnectProvider(AbstractTerraformResource):
    _group: Any
    _top_name: str
    client_id_list: Sequence[str]
    thumbprint_list: Sequence[str]
    url: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_openid_connect_provider")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
