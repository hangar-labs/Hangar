from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Parameter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="parameter")


@define(kw_only=True, slots=False)
class SsmAutomation(AbstractTerraformBlock):
    document_name: str
    role_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ssm_automation")
    document_version: Optional[str] = None
    dynamic_parameters: Optional[Dict[str, str]] = None
    parameter: Optional[Sequence[Parameter]] = None
    target_account: Optional[str] = None


@define(kw_only=True, slots=False)
class Action(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="action")
    ssm_automation: Optional[Sequence[SsmAutomation]] = None


@define(kw_only=True, slots=False)
class NotificationTarget(AbstractTerraformBlock):
    sns_topic_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="notification_target")


@define(kw_only=True, slots=False)
class IncidentTemplate(AbstractTerraformBlock):
    impact: int
    title: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="incident_template")
    dedupe_string: Optional[str] = None
    incident_tags: Optional[Dict[str, str]] = None
    notification_target: Optional[Sequence[NotificationTarget]] = None
    summary: Optional[str] = None


@define(kw_only=True, slots=False)
class Pagerduty(AbstractTerraformBlock):
    name: str
    secret_id: str
    service_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="pagerduty")


@define(kw_only=True, slots=False)
class Integration(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="integration")
    pagerduty: Optional[Sequence[Pagerduty]] = None


@define(kw_only=True, slots=False)
class AwsSsmincidentsResponsePlan(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssmincidents_response_plan")
    action: Optional[Sequence[Action]] = None
    chat_channel: Optional[Sequence[str]] = None
    display_name: Optional[str] = None
    engagements: Optional[Sequence[str]] = None
    incident_template: Optional[Sequence[IncidentTemplate]] = None
    integration: Optional[Sequence[Integration]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
