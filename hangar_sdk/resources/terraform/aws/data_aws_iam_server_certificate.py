from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsIamServerCertificate(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_server_certificate")
    latest: Optional[bool] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    path_prefix: Optional[str] = None
