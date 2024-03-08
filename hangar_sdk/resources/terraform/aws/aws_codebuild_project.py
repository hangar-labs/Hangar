from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Artifacts(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="artifacts")
    artifact_identifier: Optional[str] = None
    bucket_owner_access: Optional[str] = None
    encryption_disabled: Optional[bool] = None
    location: Optional[str] = None
    name: Optional[str] = None
    namespace_type: Optional[str] = None
    override_artifact_name: Optional[bool] = None
    packaging: Optional[str] = None
    path: Optional[str] = None


@define(kw_only=True, slots=False)
class Restrictions(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="restrictions")
    compute_types_allowed: Optional[Sequence[str]] = None
    maximum_builds_allowed: Optional[int] = None


@define(kw_only=True, slots=False)
class BuildBatchConfig(AbstractTerraformBlock):
    service_role: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="build_batch_config")
    combine_artifacts: Optional[bool] = None
    restrictions: Optional[Sequence[Restrictions]] = None
    timeout_in_mins: Optional[int] = None


@define(kw_only=True, slots=False)
class Cache(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cache")
    location: Optional[str] = None
    modes: Optional[Sequence[str]] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class EnvironmentVariable(AbstractTerraformBlock):
    name: str
    value: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="environment_variable")
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class RegistryCredential(AbstractTerraformBlock):
    credential: str
    credential_provider: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="registry_credential")


@define(kw_only=True, slots=False)
class Environment(AbstractTerraformBlock):
    compute_type: str
    image: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="environment")
    certificate: Optional[str] = None
    environment_variable: Optional[Sequence[EnvironmentVariable]] = None
    image_pull_credentials_type: Optional[str] = None
    privileged_mode: Optional[bool] = None
    registry_credential: Optional[Sequence[RegistryCredential]] = None


@define(kw_only=True, slots=False)
class FileSystemLocations(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="file_system_locations")
    identifier: Optional[str] = None
    location: Optional[str] = None
    mount_options: Optional[str] = None
    mount_point: Optional[str] = None
    type: Optional[str] = None


@define(kw_only=True, slots=False)
class CloudwatchLogs(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="cloudwatch_logs")
    group_name: Optional[str] = None
    status: Optional[str] = None
    stream_name: Optional[str] = None


@define(kw_only=True, slots=False)
class S3Logs(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="s3_logs")
    bucket_owner_access: Optional[str] = None
    encryption_disabled: Optional[bool] = None
    location: Optional[str] = None
    status: Optional[str] = None


@define(kw_only=True, slots=False)
class LogsConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="logs_config")
    cloudwatch_logs: Optional[Sequence[CloudwatchLogs]] = None
    s3_logs: Optional[Sequence[S3Logs]] = None


@define(kw_only=True, slots=False)
class SecondaryArtifacts(AbstractTerraformBlock):
    artifact_identifier: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secondary_artifacts")
    bucket_owner_access: Optional[str] = None
    encryption_disabled: Optional[bool] = None
    location: Optional[str] = None
    name: Optional[str] = None
    namespace_type: Optional[str] = None
    override_artifact_name: Optional[bool] = None
    packaging: Optional[str] = None
    path: Optional[str] = None


@define(kw_only=True, slots=False)
class SecondarySourceVersion(AbstractTerraformBlock):
    source_identifier: str
    source_version: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secondary_source_version")


@define(kw_only=True, slots=False)
class BuildStatusConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="build_status_config")
    context: Optional[str] = None
    target_url: Optional[str] = None


@define(kw_only=True, slots=False)
class GitSubmodulesConfig(AbstractTerraformBlock):
    fetch_submodules: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="git_submodules_config")


@define(kw_only=True, slots=False)
class SecondarySources(AbstractTerraformBlock):
    source_identifier: str
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="secondary_sources")
    build_status_config: Optional[Sequence[BuildStatusConfig]] = None
    buildspec: Optional[str] = None
    git_clone_depth: Optional[int] = None
    git_submodules_config: Optional[Sequence[GitSubmodulesConfig]] = None
    insecure_ssl: Optional[bool] = None
    location: Optional[str] = None
    report_build_status: Optional[bool] = None


@define(kw_only=True, slots=False)
class BuildStatusConfig(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="build_status_config")
    context: Optional[str] = None
    target_url: Optional[str] = None


@define(kw_only=True, slots=False)
class GitSubmodulesConfig(AbstractTerraformBlock):
    fetch_submodules: bool
    _block_type: str = "block"
    _name: str = field(alias="_name", default="git_submodules_config")


@define(kw_only=True, slots=False)
class Source(AbstractTerraformBlock):
    type: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="source")
    build_status_config: Optional[Sequence[BuildStatusConfig]] = None
    buildspec: Optional[str] = None
    git_clone_depth: Optional[int] = None
    git_submodules_config: Optional[Sequence[GitSubmodulesConfig]] = None
    insecure_ssl: Optional[bool] = None
    location: Optional[str] = None
    report_build_status: Optional[bool] = None


@define(kw_only=True, slots=False)
class VpcConfig(AbstractTerraformBlock):
    security_group_ids: Sequence[str]
    subnets: Sequence[str]
    vpc_id: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="vpc_config")


@define(kw_only=True, slots=False)
class AwsCodebuildProject(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    service_role: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_codebuild_project")
    artifacts: Optional[Sequence[Artifacts]] = None
    badge_enabled: Optional[bool] = None
    build_batch_config: Optional[Sequence[BuildBatchConfig]] = None
    build_timeout: Optional[int] = None
    cache: Optional[Sequence[Cache]] = None
    concurrent_build_limit: Optional[int] = None
    description: Optional[str] = None
    encryption_key: Optional[str] = None
    environment: Optional[Sequence[Environment]] = None
    file_system_locations: Optional[Sequence[FileSystemLocations]] = None
    logs_config: Optional[Sequence[LogsConfig]] = None
    project_visibility: Optional[str] = None
    queued_timeout: Optional[int] = None
    resource_access_role: Optional[str] = None
    secondary_artifacts: Optional[Sequence[SecondaryArtifacts]] = None
    secondary_source_version: Optional[Sequence[SecondarySourceVersion]] = None
    secondary_sources: Optional[Sequence[SecondarySources]] = None
    source: Optional[Sequence[Source]] = None
    source_version: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    vpc_config: Optional[Sequence[VpcConfig]] = None
