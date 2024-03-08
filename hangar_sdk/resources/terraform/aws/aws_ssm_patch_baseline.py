from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class PatchFilter(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="patch_filter")


@define(kw_only=True, slots=False)
class ApprovalRule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="approval_rule")
    approve_after_days: Optional[int] = None
    approve_until_date: Optional[str] = None
    compliance_level: Optional[str] = None
    enable_non_security: Optional[bool] = None
    patch_filter: Optional[Sequence[PatchFilter]] = None


@define(kw_only=True, slots=False)
class GlobalFilter(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="global_filter")


@define(kw_only=True, slots=False)
class Source(AbstractTerraformBlock):
    configuration: str
    name: str
    products: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source")


@define(kw_only=True, slots=False)
class AwsSsmPatchBaseline(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_patch_baseline")
    approval_rule: Optional[Sequence[ApprovalRule]] = None
    approved_patches: Optional[Sequence[str]] = None
    approved_patches_compliance_level: Optional[str] = None
    approved_patches_enable_non_security: Optional[bool] = None
    description: Optional[str] = None
    global_filter: Optional[Sequence[GlobalFilter]] = None
    operating_system: Optional[str] = None
    rejected_patches: Optional[Sequence[str]] = None
    rejected_patches_action: Optional[str] = None
    source: Optional[Sequence[Source]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
