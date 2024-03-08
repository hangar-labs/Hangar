from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RotationRules(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rotation_rules")
    automatically_after_days: Optional[int] = None
    duration: Optional[str] = None
    schedule_expression: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSecretsmanagerSecretRotation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    secret_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_secretsmanager_secret_rotation")
    rotate_immediately: Optional[bool] = None
    rotation_lambda_arn: Optional[str] = None
    rotation_rules: Optional[Sequence[RotationRules]] = None
