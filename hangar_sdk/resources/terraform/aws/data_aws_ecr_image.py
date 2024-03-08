from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsEcrImage(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    repository_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ecr_image")
    image_digest: Optional[str] = None
    image_tag: Optional[str] = None
    most_recent: Optional[bool] = None
    registry_id: Optional[str] = None
