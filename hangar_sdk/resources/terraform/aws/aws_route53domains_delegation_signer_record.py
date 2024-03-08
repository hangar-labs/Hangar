from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class SigningAttributes(AbstractTerraformBlock):
    algorithm: int
    flags: int
    public_key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="signing_attributes")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53domainsDelegationSignerRecord(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53domains_delegation_signer_record"
    )
    signing_attributes: Optional[Sequence[SigningAttributes]] = None
    timeouts: Optional[Timeouts] = None
