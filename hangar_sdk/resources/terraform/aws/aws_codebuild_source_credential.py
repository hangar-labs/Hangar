from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsCodebuildSourceCredential(AbstractTerraformResource):
    _group: Any
    _top_name: str
    auth_type: str
    server_type: str
    token: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codebuild_source_credential")
    user_name: Optional[str] = None
