from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DashboardAttributes(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dashboard_attributes")
    engagement_metrics: Optional[str] = None


@define(kw_only=True, slots=False)
class GuardianAttributes(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="guardian_attributes")
    optimized_shared_delivery: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesv2AccountVdmAttributes(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vdm_enabled: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sesv2_account_vdm_attributes")
    dashboard_attributes: Optional[Sequence[DashboardAttributes]] = None
    guardian_attributes: Optional[Sequence[GuardianAttributes]] = None
