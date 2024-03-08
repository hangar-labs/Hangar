from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class RuleConfig(AbstractTerraformBlock):
    inverted: bool
    threshold: int
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="rule_config")


@define(kw_only=True, slots=False)
class AwsRoute53recoverycontrolconfigSafetyRule(AbstractTerraformResource):
    _group: Any
    _top_name: str
    control_panel_arn: str
    name: str
    wait_period_ms: int
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_route53recoverycontrolconfig_safety_rule"
    )
    asserted_controls: Optional[Sequence[str]] = None
    gating_controls: Optional[Sequence[str]] = None
    rule_config: Optional[Sequence[RuleConfig]] = None
    target_controls: Optional[Sequence[str]] = None
