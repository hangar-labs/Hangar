from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AuthenticationOptions(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="authentication_options")
    active_directory_id: Optional[str] = None
    root_certificate_chain_arn: Optional[str] = None
    saml_provider_arn: Optional[str] = None
    self_service_saml_provider_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class ClientConnectOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="client_connect_options")
    enabled: Optional[bool] = None
    lambda_function_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class ClientLoginBannerOptions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="client_login_banner_options")
    banner_text: Optional[str] = None
    enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class ConnectionLogOptions(AbstractTerraformBlock):
    enabled: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="connection_log_options")
    cloudwatch_log_group: Optional[str] = None
    cloudwatch_log_stream: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2ClientVpnEndpoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    client_cidr_block: str
    server_certificate_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_client_vpn_endpoint")
    authentication_options: Optional[Sequence[AuthenticationOptions]] = None
    client_connect_options: Optional[Sequence[ClientConnectOptions]] = None
    client_login_banner_options: Optional[Sequence[ClientLoginBannerOptions]] = None
    connection_log_options: Optional[Sequence[ConnectionLogOptions]] = None
    description: Optional[str] = None
    dns_servers: Optional[Sequence[str]] = None
    security_group_ids: Optional[Sequence[str]] = None
    self_service_portal: Optional[str] = None
    session_timeout_hours: Optional[int] = None
    split_tunnel: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    transport_protocol: Optional[str] = None
    vpc_id: Optional[str] = None
    vpn_port: Optional[int] = None
