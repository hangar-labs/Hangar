from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Auth(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="auth")
    auth_scheme: Optional[str] = None
    client_password_auth_type: Optional[str] = None
    description: Optional[str] = None
    iam_auth: Optional[str] = None
    secret_arn: Optional[str] = None
    username: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbProxy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    engine_family: str
    name: str
    role_arn: str
    vpc_subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_proxy")
    auth: Optional[Sequence[Auth]] = None
    debug_logging: Optional[bool] = None
    idle_client_timeout: Optional[int] = None
    require_tls: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    vpc_security_group_ids: Optional[Sequence[str]] = None
