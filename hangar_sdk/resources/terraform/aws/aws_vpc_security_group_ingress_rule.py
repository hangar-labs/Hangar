from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcSecurityGroupIngressRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ip_protocol: str
    security_group_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_vpc_security_group_ingress_rule")
    cidr_ipv4: Optional[str] = None
    cidr_ipv6: Optional[str] = None
    description: Optional[str] = None
    from_port: Optional[int] = None
    prefix_list_id: Optional[str] = None
    referenced_security_group_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    to_port: Optional[int] = None
