from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


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
class AwsS3BucketServerSideEncryptionConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3_bucket_server_side_encryption_configuration"
    )
    expected_bucket_owner: Optional[str] = None
    rule: Optional[Sequence[Rule]] = None
