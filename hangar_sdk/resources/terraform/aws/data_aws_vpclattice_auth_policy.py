from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsVpclatticeAuthPolicy(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    resource_identifier: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_vpclattice_auth_policy")
    policy: Optional[str] = None
    state: Optional[str] = None
