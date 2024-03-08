from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    pattern: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    exclude_matched_pattern: Optional[bool] = None


@define(kw_only=True, slots=False)
class FilterGroup(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter_group")
    filter: Optional[Sequence[Filter]] = None


@define(kw_only=True, slots=False)
class AwsCodebuildWebhook(AbstractTerraformResource):
    _group: Any
    _top_name: str
    project_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codebuild_webhook")
    branch_filter: Optional[str] = None
    build_type: Optional[str] = None
    filter_group: Optional[Sequence[FilterGroup]] = None
