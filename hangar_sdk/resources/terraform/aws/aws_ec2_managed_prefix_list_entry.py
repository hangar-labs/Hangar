from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2ManagedPrefixListEntry(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cidr: str
    prefix_list_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_managed_prefix_list_entry")
    description: Optional[str] = None
