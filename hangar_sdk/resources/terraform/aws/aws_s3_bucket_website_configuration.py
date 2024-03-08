from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class ErrorDocument(AbstractTerraformBlock):
    key: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="error_document")


@define(kw_only=True, slots=False)
class IndexDocument(AbstractTerraformBlock):
    suffix: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="index_document")


@define(kw_only=True, slots=False)
class RedirectAllRequestsTo(AbstractTerraformBlock):
    host_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="redirect_all_requests_to")
    protocol: Optional[str] = None


@define(kw_only=True, slots=False)
class Condition(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="condition")
    http_error_code_returned_equals: Optional[str] = None
    key_prefix_equals: Optional[str] = None


@define(kw_only=True, slots=False)
class Redirect(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="redirect")
    host_name: Optional[str] = None
    http_redirect_code: Optional[str] = None
    protocol: Optional[str] = None
    replace_key_prefix_with: Optional[str] = None
    replace_key_with: Optional[str] = None


@define(kw_only=True, slots=False)
class RoutingRule(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="routing_rule")
    condition: Optional[Sequence[Condition]] = None
    redirect: Optional[Sequence[Redirect]] = None


@define(kw_only=True, slots=False)
class AwsS3BucketWebsiteConfiguration(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_bucket_website_configuration")
    error_document: Optional[Sequence[ErrorDocument]] = None
    expected_bucket_owner: Optional[str] = None
    index_document: Optional[Sequence[IndexDocument]] = None
    redirect_all_requests_to: Optional[Sequence[RedirectAllRequestsTo]] = None
    routing_rule: Optional[Sequence[RoutingRule]] = None
    routing_rules: Optional[str] = None
