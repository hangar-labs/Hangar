from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Targets(AbstractTerraformBlock):
    key: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="targets")


@define(kw_only=True, slots=False)
class Parameter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="parameter")


@define(kw_only=True, slots=False)
class AutomationParameters(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="automation_parameters")
    document_version: Optional[str] = None
    parameter: Optional[Sequence[Parameter]] = None


@define(kw_only=True, slots=False)
class LambdaParameters(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="lambda_parameters")
    client_context: Optional[str] = None
    payload: Optional[str] = None
    qualifier: Optional[str] = None


@define(kw_only=True, slots=False)
class CloudwatchConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloudwatch_config")
    cloudwatch_log_group_name: Optional[str] = None
    cloudwatch_output_enabled: Optional[bool] = None


@define(kw_only=True, slots=False)
class NotificationConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="notification_config")
    notification_arn: Optional[str] = None
    notification_events: Optional[Sequence[str]] = None
    notification_type: Optional[str] = None


@define(kw_only=True, slots=False)
class Parameter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="parameter")


@define(kw_only=True, slots=False)
class RunCommandParameters(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="run_command_parameters")
    cloudwatch_config: Optional[Sequence[CloudwatchConfig]] = None
    comment: Optional[str] = None
    document_hash: Optional[str] = None
    document_hash_type: Optional[str] = None
    document_version: Optional[str] = None
    notification_config: Optional[Sequence[NotificationConfig]] = None
    output_s3_bucket: Optional[str] = None
    output_s3_key_prefix: Optional[str] = None
    parameter: Optional[Sequence[Parameter]] = None
    service_role_arn: Optional[str] = None
    timeout_seconds: Optional[int] = None


@define(kw_only=True, slots=False)
class StepFunctionsParameters(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="step_functions_parameters")
    input: Optional[str] = None
    name: Optional[str] = None


@define(kw_only=True, slots=False)
class TaskInvocationParameters(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="task_invocation_parameters")
    automation_parameters: Optional[Sequence[AutomationParameters]] = None
    lambda_parameters: Optional[Sequence[LambdaParameters]] = None
    run_command_parameters: Optional[Sequence[RunCommandParameters]] = None
    step_functions_parameters: Optional[Sequence[StepFunctionsParameters]] = None


@define(kw_only=True, slots=False)
class AwsSsmMaintenanceWindowTask(AbstractTerraformResource):
    _group: Any
    _top_name: str
    task_arn: str
    task_type: str
    window_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssm_maintenance_window_task")
    cutoff_behavior: Optional[str] = None
    description: Optional[str] = None
    max_concurrency: Optional[str] = None
    max_errors: Optional[str] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    service_role_arn: Optional[str] = None
    targets: Optional[Sequence[Targets]] = None
    task_invocation_parameters: Optional[Sequence[TaskInvocationParameters]] = None
