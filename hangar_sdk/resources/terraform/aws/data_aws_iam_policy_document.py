from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Condition(AbstractTerraformBlock):
    test: str
    values: Sequence[str]
    variable: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="condition")


@define(kw_only=True, slots=False)
class NotPrincipals(AbstractTerraformBlock):
    identifiers: Sequence[str]
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="not_principals")


@define(kw_only=True, slots=False)
class Principals(AbstractTerraformBlock):
    identifiers: Sequence[str]
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="principals")


@define(kw_only=True, slots=False)
class Statement(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="statement")
    actions: Optional[Sequence[str]] = None
    condition: Optional[Sequence[Condition]] = None
    effect: Optional[str] = None
    not_actions: Optional[Sequence[str]] = None
    not_principals: Optional[Sequence[NotPrincipals]] = None
    not_resources: Optional[Sequence[str]] = None
    principals: Optional[Sequence[Principals]] = None
    resources: Optional[Sequence[str]] = None
    sid: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsIamPolicyDocument(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_policy_document")
    override_policy_documents: Optional[Sequence[str]] = None
    policy_id: Optional[str] = None
    source_policy_documents: Optional[Sequence[str]] = None
    statement: Optional[Sequence[Statement]] = None
    version: Optional[str] = None
