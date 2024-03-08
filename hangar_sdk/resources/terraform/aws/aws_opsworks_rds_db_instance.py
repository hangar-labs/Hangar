from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsOpsworksRdsDbInstance(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_password: str
    db_user: str
    rds_db_instance_arn: str
    stack_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_opsworks_rds_db_instance")
