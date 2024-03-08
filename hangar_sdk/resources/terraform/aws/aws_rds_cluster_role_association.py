from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRdsClusterRoleAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    db_cluster_identifier: str
    feature_name: str
    role_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_rds_cluster_role_association")
    timeouts: Optional[Timeouts] = None
