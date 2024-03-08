from typing import Any, Dict, Optional

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
class AwsDynamodbTableReplica(AbstractTerraformResource):
    _group: Any
    _top_name: str
    global_table_arn: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_dynamodb_table_replica")
    kms_key_arn: Optional[str] = None
    point_in_time_recovery: Optional[bool] = None
    table_class_override: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
