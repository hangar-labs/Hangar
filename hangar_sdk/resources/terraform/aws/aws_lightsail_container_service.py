from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EcrImagePullerRole(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ecr_image_puller_role")
    is_active: Optional[bool] = None


@define(kw_only=True, slots=False)
class PrivateRegistryAccess(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="private_registry_access")
    ecr_image_puller_role: Optional[Sequence[EcrImagePullerRole]] = None


@define(kw_only=True, slots=False)
class Certificate(AbstractTerraformBlock):
    certificate_name: str
    domain_names: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="certificate")


@define(kw_only=True, slots=False)
class PublicDomainNames(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="public_domain_names")
    certificate: Optional[Sequence[Certificate]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLightsailContainerService(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    power: str
    scale: int
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_container_service")
    is_disabled: Optional[bool] = None
    private_registry_access: Optional[Sequence[PrivateRegistryAccess]] = None
    public_domain_names: Optional[Sequence[PublicDomainNames]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
