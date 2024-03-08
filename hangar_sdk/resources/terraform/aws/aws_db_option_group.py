from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class OptionSettings(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="option_settings")


@define(kw_only=True, slots=False)
class Option(AbstractTerraformBlock):
    option_name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="option")
    db_security_group_memberships: Optional[Sequence[str]] = None
    option_settings: Optional[Sequence[OptionSettings]] = None
    port: Optional[int] = None
    version: Optional[str] = None
    vpc_security_group_memberships: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    delete: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsDbOptionGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    engine_name: str
    major_engine_version: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_db_option_group")
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    option: Optional[Sequence[Option]] = None
    option_group_description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
