from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSnsTopicDataProtectionPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    arn: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sns_topic_data_protection_policy")
