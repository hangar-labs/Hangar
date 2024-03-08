from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSesv2EmailIdentity(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    email_identity: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_sesv2_email_identity")
    tags: Optional[Dict[str, str]] = None
