from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLambdaInvocation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    input: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_invocation")
    lifecycle_scope: Optional[str] = None
    qualifier: Optional[str] = None
    terraform_key: Optional[str] = None
    triggers: Optional[Dict[str, str]] = None
