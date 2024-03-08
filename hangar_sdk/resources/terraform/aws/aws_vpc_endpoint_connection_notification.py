from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsVpcEndpointConnectionNotification(AbstractTerraformResource):
    _group: Any
    _top_name: str
    connection_events: Sequence[str]
    connection_notification_arn: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_vpc_endpoint_connection_notification"
    )
    vpc_endpoint_id: Optional[str] = None
    vpc_endpoint_service_id: Optional[str] = None
