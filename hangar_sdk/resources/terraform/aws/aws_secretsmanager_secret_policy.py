from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSecretsmanagerSecretPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    secret_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_secretsmanager_secret_policy")
    block_public_policy: Optional[bool] = None
