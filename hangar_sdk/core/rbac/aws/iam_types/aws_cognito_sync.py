from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cognito_sync_privilege_type = Union[Literal["DescribeDataset"], Literal["RegisterDevice"], Literal["ListIdentityPoolUsage"], Literal["QueryRecords"], Literal["SetDatasetConfiguration"], Literal["GetIdentityPoolConfiguration"], Literal["DescribeIdentityPoolUsage"], Literal["GetBulkPublishDetails"], Literal["DescribeIdentityUsage"], Literal["SetCognitoEvents"], Literal["SetIdentityPoolConfiguration"], Literal["BulkPublish"], Literal["GetCognitoEvents"], Literal["SubscribeToDataset"], Literal["UnsubscribeFromDataset"], Literal["ListDatasets"], Literal["DeleteDataset"], Literal["ListRecords"], Literal["UpdateRecords"]]
aws_cognito_sync_condition_type = None

class aws_cognito_syncStatement(GenericResourceType[aws_cognito_sync_privilege_type, aws_cognito_sync_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    