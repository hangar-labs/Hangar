from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EbsBlockDevice(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs_block_device")


@define(kw_only=True, slots=False)
class EphemeralBlockDevice(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ephemeral_block_device")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsAmiCopy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    source_ami_id: str
    source_ami_region: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ami_copy")
    deprecation_time: Optional[str] = None
    description: Optional[str] = None
    destination_outpost_arn: Optional[str] = None
    ebs_block_device: Optional[Sequence[EbsBlockDevice]] = None
    encrypted: Optional[bool] = None
    ephemeral_block_device: Optional[Sequence[EphemeralBlockDevice]] = None
    kms_key_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
