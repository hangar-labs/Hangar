from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AuthenticateCognito(AbstractTerraformBlock):
    user_pool_arn: str
    user_pool_client_id: str
    user_pool_domain: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authenticate_cognito")
    authentication_request_extra_params: Optional[Dict[str, str]] = None
    on_unauthenticated_request: Optional[str] = None
    scope: Optional[str] = None
    session_cookie_name: Optional[str] = None
    session_timeout: Optional[int] = None


@define(kw_only=True, slots=False)
class AuthenticateOidc(AbstractTerraformBlock):
    authorization_endpoint: str
    client_id: str
    client_secret: str
    issuer: str
    token_endpoint: str
    user_info_endpoint: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authenticate_oidc")
    authentication_request_extra_params: Optional[Dict[str, str]] = None
    on_unauthenticated_request: Optional[str] = None
    scope: Optional[str] = None
    session_cookie_name: Optional[str] = None
    session_timeout: Optional[int] = None


@define(kw_only=True, slots=False)
class FixedResponse(AbstractTerraformBlock):
    content_type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="fixed_response")
    message_body: Optional[str] = None
    status_code: Optional[str] = None


@define(kw_only=True, slots=False)
class Stickiness(AbstractTerraformBlock):
    duration: int
    _block_type: str = "block"
    _name: str = field(alias="_name", default="stickiness")
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class TargetGroup(AbstractTerraformBlock):
    arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="target_group")
    weight: Optional[int] = None


@define(kw_only=True, slots=False)
class Forward(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forward")
    stickiness: Optional[Sequence[Stickiness]] = None
    target_group: Optional[Sequence[TargetGroup]] = None


@define(kw_only=True, slots=False)
class Redirect(AbstractTerraformBlock):
    status_code: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="redirect")
    host: Optional[str] = None
    path: Optional[str] = None
    port: Optional[str] = None
    protocol: Optional[str] = None
    query: Optional[str] = None


@define(kw_only=True, slots=False)
class DefaultAction(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_action")
    authenticate_cognito: Optional[Sequence[AuthenticateCognito]] = None
    authenticate_oidc: Optional[Sequence[AuthenticateOidc]] = None
    fixed_response: Optional[Sequence[FixedResponse]] = None
    forward: Optional[Sequence[Forward]] = None
    order: Optional[int] = None
    redirect: Optional[Sequence[Redirect]] = None
    target_group_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class MutualAuthentication(AbstractTerraformBlock):
    mode: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="mutual_authentication")
    ignore_client_certificate_expiry: Optional[bool] = None
    trust_store_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsAlbListener(AbstractTerraformResource):
    _group: Any
    _top_name: str
    load_balancer_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_alb_listener")
    alpn_policy: Optional[str] = None
    certificate_arn: Optional[str] = None
    default_action: Optional[Sequence[DefaultAction]] = None
    mutual_authentication: Optional[Sequence[MutualAuthentication]] = None
    port: Optional[int] = None
    protocol: Optional[str] = None
    ssl_policy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
