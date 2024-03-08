from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DeleteMarkerReplication(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="delete_marker_replication")


@define(kw_only=True, slots=False)
class AccessControlTranslation(AbstractTerraformBlock):
    owner: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="access_control_translation")


@define(kw_only=True, slots=False)
class EncryptionConfiguration(AbstractTerraformBlock):
    replica_kms_key_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="encryption_configuration")


@define(kw_only=True, slots=False)
class EventThreshold(AbstractTerraformBlock):
    minutes: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="event_threshold")


@define(kw_only=True, slots=False)
class Metrics(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="metrics")
    event_threshold: Optional[Sequence[EventThreshold]] = None


@define(kw_only=True, slots=False)
class Time(AbstractTerraformBlock):
    minutes: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="time")


@define(kw_only=True, slots=False)
class ReplicationTime(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replication_time")
    time: Optional[Sequence[Time]] = None


@define(kw_only=True, slots=False)
class Destination(AbstractTerraformBlock):
    bucket: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="destination")
    access_control_translation: Optional[Sequence[AccessControlTranslation]] = None
    account: Optional[str] = None
    encryption_configuration: Optional[Sequence[EncryptionConfiguration]] = None
    metrics: Optional[Sequence[Metrics]] = None
    replication_time: Optional[Sequence[ReplicationTime]] = None
    storage_class: Optional[str] = None


@define(kw_only=True, slots=False)
class ExistingObjectReplication(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="existing_object_replication")


@define(kw_only=True, slots=False)
class Tag(AbstractTerraformBlock):
    key: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="tag")


@define(kw_only=True, slots=False)
class TerraformAnd(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="terraform_and")
    prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")
    prefix: Optional[str] = None
    tag: Optional[Sequence[Tag]] = None
    terraform_and: Optional[Sequence[TerraformAnd]] = None


@define(kw_only=True, slots=False)
class ReplicaModifications(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="replica_modifications")


@define(kw_only=True, slots=False)
class SseKmsEncryptedObjects(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="sse_kms_encrypted_objects")


@define(kw_only=True, slots=False)
class SourceSelectionCriteria(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_selection_criteria")
    replica_modifications: Optional[Sequence[ReplicaModifications]] = None
    sse_kms_encrypted_objects: Optional[Sequence[SseKmsEncryptedObjects]] = None


@define(kw_only=True, slots=False)
class Rule(AbstractTerraformBlock):
    status: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule")
    delete_marker_replication: Optional[Sequence[DeleteMarkerReplication]] = None
    destination: Optional[Sequence[Destination]] = None
    existing_object_replication: Optional[Sequence[ExistingObjectReplication]] = None
    filter: Optional[Sequence[Filter]] = None
    prefix: Optional[str] = None
    priority: Optional[int] = None
    source_selection_criteria: Optional[Sequence[SourceSelectionCriteria]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketReplicationConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    role: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_replication_configuration")
    rule: Optional[Sequence[Rule]] = None
    token: Optional[str] = None
