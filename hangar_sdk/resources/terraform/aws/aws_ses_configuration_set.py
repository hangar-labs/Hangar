from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DeliveryOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="delivery_options")
    tls_policy: Optional[str] = None


@define(kw_only=True, slots=False)
class TrackingOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tracking_options")
    custom_redirect_domain: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesConfigurationSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_configuration_set")
    delivery_options: Optional[Sequence[DeliveryOptions]] = None
    reputation_metrics_enabled: Optional[bool] = None
    sending_enabled: Optional[bool] = None
    tracking_options: Optional[Sequence[TrackingOptions]] = None
