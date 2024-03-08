from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2InstanceConnectEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    subnet_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_instance_connect_endpoint")
    preserve_client_ip: Optional[bool] = None
    security_group_ids: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
