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
class WhitelistRules(AbstractTerraformBlock):
    cidr: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="whitelist_rules")


@define(kw_only=True, slots=False)
class AwsMedialiveInputSecurityGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_medialive_input_security_group")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
    whitelist_rules: Optional[Sequence[WhitelistRules]] = None
