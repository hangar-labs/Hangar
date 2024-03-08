from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CatalogData(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="catalog_data")
    about_text: Optional[str] = None
    architectures: Optional[Sequence[str]] = None
    description: Optional[str] = None
    logo_image_blob: Optional[str] = None
    operating_systems: Optional[Sequence[str]] = None
    usage_text: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEcrpublicRepository(AbstractTerraformResource):
    _group: Any
    _top_name: str
    repository_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecrpublic_repository")
    catalog_data: Optional[Sequence[CatalogData]] = None
    force_destroy: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
