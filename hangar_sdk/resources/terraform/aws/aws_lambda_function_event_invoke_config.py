from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class OnFailure(AbstractTerraformBlock):
    destination: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="on_failure")


@define(kw_only=True, slots=False)
class OnSuccess(AbstractTerraformBlock):
    destination: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="on_success")


@define(kw_only=True, slots=False)
class DestinationConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination_config")
    on_failure: Optional[Sequence[OnFailure]] = None
    on_success: Optional[Sequence[OnSuccess]] = None


@define(kw_only=True, slots=False)
class AwsLambdaFunctionEventInvokeConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_function_event_invoke_config")
    destination_config: Optional[Sequence[DestinationConfig]] = None
    maximum_event_age_in_seconds: Optional[int] = None
    maximum_retry_attempts: Optional[int] = None
    qualifier: Optional[str] = None
