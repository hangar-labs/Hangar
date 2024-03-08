from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AllowedPublishers(AbstractTerraformBlock):
    signing_profile_version_arns: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="allowed_publishers")


@define(kw_only=True, slots=False)
class Policies(AbstractTerraformBlock):
    untrusted_artifact_on_deployment: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="policies")


@define(kw_only=True, slots=False)
class AwsLambdaCodeSigningConfig(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_lambda_code_signing_config")
    allowed_publishers: Optional[Sequence[AllowedPublishers]] = None
    description: Optional[str] = None
    policies: Optional[Sequence[Policies]] = None
