from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLambdaProvisionedConcurrencyConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_name: str
    provisioned_concurrent_executions: int
    qualifier: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_lambda_provisioned_concurrency_config"
    )
    skip_destroy: Optional[bool] = None
    timeouts: Optional[Timeouts] = None
