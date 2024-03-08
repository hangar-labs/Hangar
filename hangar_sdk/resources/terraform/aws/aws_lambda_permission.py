from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLambdaPermission(AbstractTerraformResource):
    _group: Any
    _top_name: str
    action: str
    function_name: str
    principal: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_permission")
    event_source_token: Optional[str] = None
    function_url_auth_type: Optional[str] = None
    principal_org_id: Optional[str] = None
    qualifier: Optional[str] = None
    source_account: Optional[str] = None
    source_arn: Optional[str] = None
    statement_id: Optional[str] = None
    statement_id_prefix: Optional[str] = None
