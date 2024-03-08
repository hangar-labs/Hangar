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
class AwsAmiFromInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    source_instance_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ami_from_instance")
    deprecation_time: Optional[str] = None
    description: Optional[str] = None
    ebs_block_device: Optional[Sequence[EbsBlockDevice]] = None
    ephemeral_block_device: Optional[Sequence[EphemeralBlockDevice]] = None
    snapshot_without_reboot: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
