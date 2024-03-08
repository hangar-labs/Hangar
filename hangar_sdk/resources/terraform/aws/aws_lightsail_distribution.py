from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class CacheBehavior(AbstractTerraformBlock):
    behavior: str
    path: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cache_behavior")


@define(kw_only=True, slots=False)
class ForwardedCookies(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forwarded_cookies")
    cookies_allow_list: Optional[Sequence[str]] = None
    option: Optional[str] = None


@define(kw_only=True, slots=False)
class ForwardedHeaders(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forwarded_headers")
    headers_allow_list: Optional[Sequence[str]] = None
    option: Optional[str] = None


@define(kw_only=True, slots=False)
class ForwardedQueryStrings(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="forwarded_query_strings")
    option: Optional[bool] = None
    query_strings_allowed_list: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class CacheBehaviorSettings(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cache_behavior_settings")
    allowed_http_methods: Optional[str] = None
    cached_http_methods: Optional[str] = None
    default_ttl: Optional[int] = None
    forwarded_cookies: Optional[Sequence[ForwardedCookies]] = None
    forwarded_headers: Optional[Sequence[ForwardedHeaders]] = None
    forwarded_query_strings: Optional[Sequence[ForwardedQueryStrings]] = None
    maximum_ttl: Optional[int] = None
    minimum_ttl: Optional[int] = None


@define(kw_only=True, slots=False)
class DefaultCacheBehavior(AbstractTerraformBlock):
    behavior: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_cache_behavior")


@define(kw_only=True, slots=False)
class Origin(AbstractTerraformBlock):
    name: str
    region_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="origin")
    protocol_policy: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsLightsailDistribution(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bundle_id: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lightsail_distribution")
    cache_behavior: Optional[Sequence[CacheBehavior]] = None
    cache_behavior_settings: Optional[Sequence[CacheBehaviorSettings]] = None
    certificate_name: Optional[str] = None
    default_cache_behavior: Optional[Sequence[DefaultCacheBehavior]] = None
    ip_address_type: Optional[str] = None
    is_enabled: Optional[bool] = None
    origin: Optional[Sequence[Origin]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
