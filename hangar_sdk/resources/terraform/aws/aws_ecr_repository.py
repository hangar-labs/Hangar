from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class EncryptionConfiguration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="encryption_configuration")
    encryption_type: Optional[str] = None
    kms_key: Optional[str] = None


@define(kw_only=True, slots=False)
class ImageScanningConfiguration(AbstractTerraformBlock):
    scan_on_push: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="image_scanning_configuration")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEcrRepository(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecr_repository")
    encryption_configuration: Optional[Sequence[EncryptionConfiguration]] = None
    force_delete: Optional[bool] = None
    image_scanning_configuration: Optional[Sequence[ImageScanningConfiguration]] = None
    image_tag_mutability: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
