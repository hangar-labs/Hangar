from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEcrpublicRepositoryPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    repository_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ecrpublic_repository_policy")
