from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDocdbEventSubscription(AbstractTerraformResource):
    _group: Any
    _top_name: str
    sns_topic_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_docdb_event_subscription")
    enabled: Optional[bool] = None
    event_categories: Optional[Sequence[str]] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    source_ids: Optional[Sequence[str]] = None
    source_type: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
