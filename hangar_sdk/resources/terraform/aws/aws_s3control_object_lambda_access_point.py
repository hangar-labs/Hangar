from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsLambda(AbstractTerraformBlock):
    function_arn: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="aws_lambda")
    function_payload: Optional[str] = None


@define(kw_only=True, slots=False)
class ContentTransformation(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="content_transformation")
    aws_lambda: Optional[Sequence[AwsLambda]] = None


@define(kw_only=True, slots=False)
class TransformationConfiguration(AbstractTerraformBlock):
    actions: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="transformation_configuration")
    content_transformation: Optional[Sequence[ContentTransformation]] = None


@define(kw_only=True, slots=False)
class Configuration(AbstractTerraformBlock):
    supporting_access_point: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="configuration")
    allowed_features: Optional[Sequence[str]] = None
    cloud_watch_metrics_enabled: Optional[bool] = None
    transformation_configuration: Optional[Sequence[TransformationConfiguration]] = None


@define(kw_only=True, slots=False)
class AwsS3controlObjectLambdaAccessPoint(AbstractTerraformResource):
    _group: Any
    _top_name: str
    name: str
    _block_type: str = "resource"
    _name: str = field(
        alias="_name", default="aws_s3control_object_lambda_access_point"
    )
    account_id: Optional[str] = None
    configuration: Optional[Sequence[Configuration]] = None
