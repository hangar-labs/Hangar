from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DkimSigningAttributes(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dkim_signing_attributes")
    domain_signing_private_key: Optional[str] = None
    domain_signing_selector: Optional[str] = None
    next_signing_key_length: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesv2EmailIdentity(AbstractTerraformResource):
    _group: Any
    _top_name: str
    email_identity: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sesv2_email_identity")
    configuration_set_name: Optional[str] = None
    dkim_signing_attributes: Optional[Sequence[DkimSigningAttributes]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
