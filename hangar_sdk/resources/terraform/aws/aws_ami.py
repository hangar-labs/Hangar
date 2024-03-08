from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EbsBlockDevice(AbstractTerraformBlock):
    device_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ebs_block_device")
    delete_on_termination: Optional[bool] = None
    encrypted: Optional[bool] = None
    iops: Optional[int] = None
    outpost_arn: Optional[str] = None
    snapshot_id: Optional[str] = None
    throughput: Optional[int] = None
    volume_size: Optional[int] = None
    volume_type: Optional[str] = None


@define(kw_only=True, slots=False)
class EphemeralBlockDevice(AbstractTerraformBlock):
    device_name: str
    virtual_name: str
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
class AwsAmi(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ami")
    architecture: Optional[str] = None
    boot_mode: Optional[str] = None
    deprecation_time: Optional[str] = None
    description: Optional[str] = None
    ebs_block_device: Optional[Sequence[EbsBlockDevice]] = None
    ena_support: Optional[bool] = None
    ephemeral_block_device: Optional[Sequence[EphemeralBlockDevice]] = None
    image_location: Optional[str] = None
    imds_support: Optional[str] = None
    kernel_id: Optional[str] = None
    ramdisk_id: Optional[str] = None
    root_device_name: Optional[str] = None
    sriov_net_support: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    tpm_support: Optional[str] = None
    virtualization_type: Optional[str] = None
