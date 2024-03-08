from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DeliveryOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="delivery_options")
    sending_pool_name: Optional[str] = None
    tls_policy: Optional[str] = None


@define(kw_only=True, slots=False)
class ReputationOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="reputation_options")
    reputation_metrics_enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class SendingOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sending_options")
    sending_enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class SuppressionOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="suppression_options")
    suppressed_reasons: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class TrackingOptions(AbstractTerraformBlock):
    custom_redirect_domain: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tracking_options")


@define(kw_only=True, slots=False)
class DashboardOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dashboard_options")
    engagement_metrics: Optional[str] = None


@define(kw_only=True, slots=False)
class GuardianOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="guardian_options")
    optimized_shared_delivery: Optional[str] = None


@define(kw_only=True, slots=False)
class VdmOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vdm_options")
    dashboard_options: Optional[Sequence[DashboardOptions]] = None
    guardian_options: Optional[Sequence[GuardianOptions]] = None


@define(kw_only=True, slots=False)
class AwsSesv2ConfigurationSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    configuration_set_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sesv2_configuration_set")
    delivery_options: Optional[Sequence[DeliveryOptions]] = None
    reputation_options: Optional[Sequence[ReputationOptions]] = None
    sending_options: Optional[Sequence[SendingOptions]] = None
    suppression_options: Optional[Sequence[SuppressionOptions]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    tracking_options: Optional[Sequence[TrackingOptions]] = None
    vdm_options: Optional[Sequence[VdmOptions]] = None
