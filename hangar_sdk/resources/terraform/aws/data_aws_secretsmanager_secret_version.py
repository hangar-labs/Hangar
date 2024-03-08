from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSecretsmanagerSecretVersion(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    secret_id: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_secretsmanager_secret_version")
    version_id: Optional[str] = None
    version_stage: Optional[str] = None
