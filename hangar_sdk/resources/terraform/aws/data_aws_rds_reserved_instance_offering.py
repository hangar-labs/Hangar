from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsRdsReservedInstanceOffering(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    db_instance_class: str
    duration: int
    multi_az: bool
    offering_type: str
    product_description: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_rds_reserved_instance_offering")
