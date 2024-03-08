from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    read: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsEc2InstanceType(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    instance_type: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ec2_instance_type")
    timeouts: Optional[Timeouts] = None
