from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSecretsmanagerSecretVersion(AbstractTerraformResource):
    _group: Any
    _top_name: str
    secret_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_secretsmanager_secret_version")
    secret_binary: Optional[str] = None
    secret_string: Optional[str] = None
    version_stages: Optional[Sequence[str]] = None
