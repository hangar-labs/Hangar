from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsIamSamlProvider(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    arn: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_saml_provider")
    tags: Optional[Dict[str, str]] = None
