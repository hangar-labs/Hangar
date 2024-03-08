from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsEc2PublicIpv4Pool(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    pool_id: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ec2_public_ipv4_pool")
    tags: Optional[Dict[str, str]] = None
