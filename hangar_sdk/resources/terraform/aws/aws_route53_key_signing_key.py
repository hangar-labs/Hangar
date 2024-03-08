from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53KeySigningKey(AbstractTerraformResource):
    _group: Any
    _top_name: str
    hosted_zone_id: str
    key_management_service_arn: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_route53_key_signing_key")
    status: Optional[str] = None
