from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsApprunnerAutoScalingConfigurationVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    auto_scaling_configuration_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_apprunner_auto_scaling_configuration_version"
    )
    max_concurrency: Optional[int] = None
    max_size: Optional[int] = None
    min_size: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
