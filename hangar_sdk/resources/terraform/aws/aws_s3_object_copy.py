from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Grant(AbstractTerraformBlock):
    permissions: Sequence[str]
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grant")
    email: Optional[str] = None
    uri: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3ObjectCopy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    key: str
    source: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_object_copy")
    acl: Optional[str] = None
    bucket_key_enabled: Optional[bool] = None
    cache_control: Optional[str] = None
    checksum_algorithm: Optional[str] = None
    content_disposition: Optional[str] = None
    content_encoding: Optional[str] = None
    content_language: Optional[str] = None
    content_type: Optional[str] = None
    copy_if_match: Optional[str] = None
    copy_if_modified_since: Optional[str] = None
    copy_if_none_match: Optional[str] = None
    copy_if_unmodified_since: Optional[str] = None
    customer_algorithm: Optional[str] = None
    customer_key: Optional[str] = None
    customer_key_md5: Optional[str] = None
    expected_bucket_owner: Optional[str] = None
    expected_source_bucket_owner: Optional[str] = None
    expires: Optional[str] = None
    force_destroy: Optional[bool] = None
    grant: Optional[Sequence[Grant]] = None
    kms_encryption_context: Optional[str] = None
    kms_key_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    metadata_directive: Optional[str] = None
    object_lock_legal_hold_status: Optional[str] = None
    object_lock_mode: Optional[str] = None
    object_lock_retain_until_date: Optional[str] = None
    request_payer: Optional[str] = None
    server_side_encryption: Optional[str] = None
    source_customer_algorithm: Optional[str] = None
    source_customer_key: Optional[str] = None
    source_customer_key_md5: Optional[str] = None
    storage_class: Optional[str] = None
    tagging_directive: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    website_redirect: Optional[str] = None
