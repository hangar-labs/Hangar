from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsSesActiveReceiptRuleSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    rule_set_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ses_active_receipt_rule_set")
