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
class Action(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="action")
    authenticate_cognito: Optional[Sequence[AuthenticateCognito]] = None
    authenticate_oidc: Optional[Sequence[AuthenticateOidc]] = None
    fixed_response: Optional[Sequence[FixedResponse]] = None
    forward: Optional[Sequence[Forward]] = None
    order: Optional[int] = None
    redirect: Optional[Sequence[Redirect]] = None
    target_group_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class HostHeader(AbstractTerraformBlock):
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="host_header")


@define(kw_only=True, slots=False)
class HttpHeader(AbstractTerraformBlock):
    http_header_name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="http_header")


@define(kw_only=True, slots=False)
class HttpRequestMethod(AbstractTerraformBlock):
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="http_request_method")


@define(kw_only=True, slots=False)
class PathPattern(AbstractTerraformBlock):
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="path_pattern")


@define(kw_only=True, slots=False)
class QueryString(AbstractTerraformBlock):
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="query_string")
    key: Optional[str] = None


@define(kw_only=True, slots=False)
class SourceIp(AbstractTerraformBlock):
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source_ip")


@define(kw_only=True, slots=False)
class Condition(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="condition")
    host_header: Optional[Sequence[HostHeader]] = None
    http_header: Optional[Sequence[HttpHeader]] = None
    http_request_method: Optional[Sequence[HttpRequestMethod]] = None
    path_pattern: Optional[Sequence[PathPattern]] = None
    query_string: Optional[Sequence[QueryString]] = None
    source_ip: Optional[Sequence[SourceIp]] = None


@define(kw_only=True, slots=False)
class AwsAlbListenerRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    listener_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_alb_listener_rule")
    action: Optional[Sequence[Action]] = None
    condition: Optional[Sequence[Condition]] = None
    priority: Optional[int] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
