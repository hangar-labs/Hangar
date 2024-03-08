from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Topic(AbstractTerraformBlock):
    default_subscription_status: str
    display_name: str
    topic_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="topic")
    description: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSesv2ContactList(AbstractTerraformResource):
    _group: Any
    _top_name: str
    contact_list_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_sesv2_contact_list")
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    topic: Optional[Sequence[Topic]] = None
