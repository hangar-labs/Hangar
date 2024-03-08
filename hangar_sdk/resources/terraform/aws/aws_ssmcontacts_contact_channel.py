from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DeliveryAddress(AbstractTerraformBlock):
    simple_address: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="delivery_address")


@define(kw_only=True, slots=False)
class AwsSsmcontactsContactChannel(AbstractTerraformResource):
    _group: Any
    _top_name: str
    contact_id: str
    name: str
    type: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssmcontacts_contact_channel")
    delivery_address: Optional[Sequence[DeliveryAddress]] = None
