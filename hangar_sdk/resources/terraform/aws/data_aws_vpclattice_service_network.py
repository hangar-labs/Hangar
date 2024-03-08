from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsVpclatticeServiceNetwork(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    service_network_identifier: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_vpclattice_service_network")
    tags: Optional[Dict[str, str]] = None
