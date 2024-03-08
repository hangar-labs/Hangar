from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Secret(AbstractTerraformBlock):
    name: str
    payload: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secret")
    context: Optional[Dict[str, str]] = None
    grant_tokens: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class DataAwsKmsSecret(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_kms_secret")
    secret: Optional[Sequence[Secret]] = None
