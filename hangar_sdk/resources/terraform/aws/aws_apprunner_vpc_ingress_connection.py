from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class IngressVpcConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ingress_vpc_configuration")
    vpc_endpoint_id: Optional[str] = None
    vpc_id: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsApprunnerVpcIngressConnection(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    service_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_apprunner_vpc_ingress_connection")
    ingress_vpc_configuration: Optional[Sequence[IngressVpcConfiguration]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
