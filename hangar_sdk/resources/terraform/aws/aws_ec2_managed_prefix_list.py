from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Entry(AbstractTerraformBlock):
    cidr: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="entry")
    description: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsEc2ManagedPrefixList(AbstractTerraformResource):
    _group: Any
    _top_name: str
    address_family: str
    max_entries: int
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_managed_prefix_list")
    entry: Optional[Sequence[Entry]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
