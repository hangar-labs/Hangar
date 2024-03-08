from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53QueryLog(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cloudwatch_log_group_arn: str
    zone_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_query_log")
