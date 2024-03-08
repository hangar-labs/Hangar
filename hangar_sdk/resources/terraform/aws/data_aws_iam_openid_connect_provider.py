from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsIamOpenidConnectProvider(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_openid_connect_provider")
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    url: Optional[str] = None
