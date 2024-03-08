from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsRoute53recoverycontrolconfigControlPanel(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_arn: str
    name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53recoverycontrolconfig_control_panel"
    )
