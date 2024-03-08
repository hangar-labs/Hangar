from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLbTrustStore(AbstractTerraformResource):
    _group: Any
    _top_name: str
    ca_certificates_bundle_s3_bucket: str
    ca_certificates_bundle_s3_key: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lb_trust_store")
    ca_certificates_bundle_s3_object_version: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
