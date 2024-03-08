from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Options(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="options")
    appliance_mode_support: Optional[bool] = None
    ipv6_support: Optional[bool] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsNetworkmanagerVpcAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    core_network_id: str
    subnet_arns: Sequence[str]
    vpc_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_networkmanager_vpc_attachment")
    options: Optional[Sequence[Options]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
