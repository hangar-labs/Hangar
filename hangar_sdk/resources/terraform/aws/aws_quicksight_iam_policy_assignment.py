from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Identities(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="identities")
    terraform_group: Optional[Sequence[str]] = None
    user: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class AwsQuicksightIamPolicyAssignment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    assignment_name: str
    assignment_status: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_quicksight_iam_policy_assignment")
    aws_account_id: Optional[str] = None
    identities: Optional[Sequence[Identities]] = None
    namespace: Optional[str] = None
    policy_arn: Optional[str] = None
