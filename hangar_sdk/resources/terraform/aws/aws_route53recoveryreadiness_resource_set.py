from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class NlbResource(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="nlb_resource")
    arn: Optional[str] = None


@define(kw_only=True, slots=False)
class R53Resource(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="r53_resource")
    domain_name: Optional[str] = None
    record_set_id: Optional[str] = None


@define(kw_only=True, slots=False)
class TargetResource(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_resource")
    nlb_resource: Optional[Sequence[NlbResource]] = None
    r53_resource: Optional[Sequence[R53Resource]] = None


@define(kw_only=True, slots=False)
class DnsTargetResource(AbstractTerraformBlock):
    domain_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="dns_target_resource")
    hosted_zone_arn: Optional[str] = None
    record_set_id: Optional[str] = None
    record_type: Optional[str] = None
    target_resource: Optional[Sequence[TargetResource]] = None


@define(kw_only=True, slots=False)
class Resources(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="resources")
    dns_target_resource: Optional[Sequence[DnsTargetResource]] = None
    readiness_scopes: Optional[Sequence[str]] = None
    resource_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRoute53recoveryreadinessResourceSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    resource_set_name: str
    resource_set_type: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53recoveryreadiness_resource_set"
    )
    resources: Optional[Sequence[Resources]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
