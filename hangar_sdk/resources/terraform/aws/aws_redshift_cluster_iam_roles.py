from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsRedshiftClusterIamRoles(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_identifier: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_redshift_cluster_iam_roles")
    default_iam_role_arn: Optional[str] = None
    iam_role_arns: Optional[Sequence[str]] = None
    timeouts: Optional[Timeouts] = None
