from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEcrPullThroughCacheRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ecr_repository_prefix: str
    upstream_registry_url: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecr_pull_through_cache_rule")
    credential_arn: Optional[str] = None
