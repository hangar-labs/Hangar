from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class VpcOptions(AbstractTerraformBlock):
    subnet_ids: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vpc_options")
    security_group_ids: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class AwsOpensearchVpcEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    domain_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_opensearch_vpc_endpoint")
    timeouts: Optional[Timeouts] = None
    vpc_options: Optional[Sequence[VpcOptions]] = None
