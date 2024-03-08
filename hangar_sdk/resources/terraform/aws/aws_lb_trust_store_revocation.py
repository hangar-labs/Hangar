from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLbTrustStoreRevocation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    revocations_s3_bucket: str
    revocations_s3_key: str
    trust_store_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lb_trust_store_revocation")
    revocations_s3_object_version: Optional[str] = None
    timeouts: Optional[Timeouts] = None
