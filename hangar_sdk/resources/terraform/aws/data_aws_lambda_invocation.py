from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsLambdaInvocation(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    function_name: str
    input: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_lambda_invocation")
    qualifier: Optional[str] = None
