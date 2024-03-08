from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CorsRule(AbstractTerraformBlock):
    allowed_methods: Sequence[str]
    allowed_origins: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cors_rule")
    allowed_headers: Optional[Sequence[str]] = None
    expose_headers: Optional[Sequence[str]] = None
    max_age_seconds: Optional[int] = None


@define(kw_only=True, slots=False)
class Grant(AbstractTerraformBlock):
    permissions: Sequence[str]
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="grant")
    uri: Optional[str] = None


@define(kw_only=True, slots=False)
class Expiration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="expiration")
    date: Optional[str] = None
    days: Optional[int] = None
    expired_object_delete_marker: Optional[bool] = None


@define(kw_only=True, slots=False)
class NoncurrentVersionExpiration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="noncurrent_version_expiration")
    days: Optional[int] = None


@define(kw_only=True, slots=False)
class NoncurrentVersionTransition(AbstractTerraformBlock):
    storage_class: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="noncurrent_version_transition")
    days: Optional[int] = None


@define(kw_only=True, slots=False)
class Transition(AbstractTerraformBlock):
    storage_class: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="transition")
    date: Optional[str] = None
    days: Optional[int] = None


@define(kw_only=True, slots=False)
class LifecycleRule(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="lifecycle_rule")
    abort_incomplete_multipart_upload_days: Optional[int] = None
    expiration: Optional[Sequence[Expiration]] = None
    noncurrent_version_expiration: Optional[Sequence[NoncurrentVersionExpiration]] = (
        None
    )
    noncurrent_version_transition: Optional[Sequence[NoncurrentVersionTransition]] = (
        None
    )
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    transition: Optional[Sequence[Transition]] = None


@define(kw_only=True, slots=False)
class Logging(AbstractTerraformBlock):
    target_bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="logging")
    target_prefix: Optional[str] = None


@define(kw_only=True, slots=False)
class DefaultRetention(AbstractTerraformBlock):
    mode: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_retention")
    days: Optional[int] = None
    years: Optional[int] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    default_retention: Optional[Sequence[DefaultRetention]] = None


@define(kw_only=True, slots=False)
class ObjectLockConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="object_lock_configuration")
    object_lock_enabled: Optional[str] = None
    rule: Optional[Sequence[Rule]] = None


@define(kw_only=True, slots=False)
class AccessControlTranslation(AbstractTerraformBlock):
    owner: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_control_translation")


@define(kw_only=True, slots=False)
class Metrics(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metrics")
    minutes: Optional[int] = None
    status: Optional[str] = None


@define(kw_only=True, slots=False)
class ReplicationTime(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replication_time")
    minutes: Optional[int] = None
    status: Optional[str] = None


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")
    access_control_translation: Optional[Sequence[AccessControlTranslation]] = None
    account_id: Optional[str] = None
    metrics: Optional[Sequence[Metrics]] = None
    replica_kms_key_id: Optional[str] = None
    replication_time: Optional[Sequence[ReplicationTime]] = None
    storage_class: Optional[str] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class SseKmsEncryptedObjects(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sse_kms_encrypted_objects")


@define(kw_only=True, slots=False)
class SourceSelectionCriteria(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_selection_criteria")
    sse_kms_encrypted_objects: Optional[Sequence[SseKmsEncryptedObjects]] = None


@define(kw_only=True, slots=False)
class Rules(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rules")
    delete_marker_replication_status: Optional[str] = None
    destination: Optional[Sequence[Destination]] = None
    filter: Optional[Sequence[Filter]] = None
    prefix: Optional[str] = None
    priority: Optional[int] = None
    source_selection_criteria: Optional[Sequence[SourceSelectionCriteria]] = None


@define(kw_only=True, slots=False)
class ReplicationConfiguration(AbstractTerraformBlock):
    role: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replication_configuration")
    rules: Optional[Sequence[Rules]] = None


@define(kw_only=True, slots=False)
class ApplyServerSideEncryptionByDefault(AbstractTerraformBlock):
    sse_algorithm: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="apply_server_side_encryption_by_default")
    kms_master_key_id: Optional[str] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    apply_server_side_encryption_by_default: Optional[
        Sequence[ApplyServerSideEncryptionByDefault]
    ] = None
    bucket_key_enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class ServerSideEncryptionConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="server_side_encryption_configuration")
    rule: Optional[Sequence[Rule]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    read: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class Versioning(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="versioning")
    enabled: Optional[bool] = None
    mfa_delete: Optional[bool] = None


@define(kw_only=True, slots=False)
class Website(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="website")
    error_document: Optional[str] = None
    index_document: Optional[str] = None
    redirect_all_requests_to: Optional[str] = None
    routing_rules: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsS3Bucket(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket")
    acceleration_status: Optional[str] = None
    acl: Optional[str] = None
    bucket: Optional[str] = None
    bucket_prefix: Optional[str] = None
    cors_rule: Optional[Sequence[CorsRule]] = None
    force_destroy: Optional[bool] = None
    grant: Optional[Sequence[Grant]] = None
    lifecycle_rule: Optional[Sequence[LifecycleRule]] = None
    logging: Optional[Sequence[Logging]] = None
    object_lock_configuration: Optional[Sequence[ObjectLockConfiguration]] = None
    object_lock_enabled: Optional[bool] = None
    policy: Optional[str] = None
    replication_configuration: Optional[Sequence[ReplicationConfiguration]] = None
    request_payer: Optional[str] = None
    server_side_encryption_configuration: Optional[
        Sequence[ServerSideEncryptionConfiguration]
    ] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    versioning: Optional[Sequence[Versioning]] = None
    website: Optional[Sequence[Website]] = None
