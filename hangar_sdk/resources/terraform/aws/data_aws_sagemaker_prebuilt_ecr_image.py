from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSagemakerPrebuiltEcrImage(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    repository_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_sagemaker_prebuilt_ecr_image")
    dns_suffix: Optional[str] = None
    image_tag: Optional[str] = None
    region: Optional[str] = None
