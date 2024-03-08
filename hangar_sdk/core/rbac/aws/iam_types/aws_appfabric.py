from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_appfabric_privilege_type = Union[Literal["DeleteIngestion"], Literal["StartUserAccessTasks"], Literal["UntagResource"], Literal["GetIngestionDestination"], Literal["ListIngestions"], Literal["CreateIngestion"], Literal["DeleteAppBundle"], Literal["UpdateAppAuthorization"], Literal["CreateAppAuthorization"], Literal["ListTagsForResource"], Literal["StartIngestion"], Literal["StopIngestion"], Literal["DeleteIngestionDestination"], Literal["BatchGetUserAccessTasks"], Literal["UpdateIngestionDestination"], Literal["ConnectAppAuthorization"], Literal["ListAppAuthorizations"], Literal["ListAppBundles"], Literal["GetIngestion"], Literal["GetAppAuthorization"], Literal["TagResource"], Literal["DeleteAppAuthorization"], Literal["GetAppBundle"], Literal["CreateIngestionDestination"], Literal["CreateAppBundle"], Literal["ListIngestionDestinations"]]
aws_appfabric_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_appfabricStatement(GenericResourceType[aws_appfabric_privilege_type, aws_appfabric_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    