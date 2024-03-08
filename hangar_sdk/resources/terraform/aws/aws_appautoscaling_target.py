from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsAppautoscalingTarget(AbstractTerraformResource):
    _group: Any
    _top_name: str
    max_capacity: int
    min_capacity: int
    resource_id: str
    scalable_dimension: str
    service_namespace: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_appautoscaling_target")
    role_arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
