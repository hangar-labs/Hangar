from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsDbInstanceRoleAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_instance_identifier: str
    feature_name: str
    role_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_instance_role_association")
