from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsNeptuneOrderableDbInstance(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_neptune_orderable_db_instance")
    engine: Optional[str] = None
    engine_version: Optional[str] = None
    instance_class: Optional[str] = None
    license_model: Optional[str] = None
    preferred_instance_classes: Optional[Sequence[str]] = None
    vpc: Optional[bool] = None
