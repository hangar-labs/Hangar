from typing import Any, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsMskScramSecretAssociation(AbstractTerraformResource):
    _group: Any
    _top_name: str
    cluster_arn: str
    secret_arn_list: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_msk_scram_secret_association")
