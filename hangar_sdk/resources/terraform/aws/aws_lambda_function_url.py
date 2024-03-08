from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Cors(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cors")
    allow_credentials: Optional[bool] = None
    allow_headers: Optional[Sequence[str]] = None
    allow_methods: Optional[Sequence[str]] = None
    allow_origins: Optional[Sequence[str]] = None
    expose_headers: Optional[Sequence[str]] = None
    max_age: Optional[int] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLambdaFunctionUrl(AbstractTerraformResource):
    _group: Any
    _top_name: str
    authorization_type: str
    function_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_function_url")
    cors: Optional[Sequence[Cors]] = None
    invoke_mode: Optional[str] = None
    qualifier: Optional[str] = None
    timeouts: Optional[Timeouts] = None
