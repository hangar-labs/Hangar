from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsConnectLambdaFunctionAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    function_arn: str
    instance_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_connect_lambda_function_association")
