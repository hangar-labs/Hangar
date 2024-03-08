from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApprunnerDefaultAutoScalingConfigurationVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    auto_scaling_configuration_arn: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name",
        default="aws_apprunner_default_auto_scaling_configuration_version",
    )
