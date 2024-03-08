from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_dataexchange_privilege_type = Union[Literal["GetDataSet"], Literal["UntagResource"], Literal["CreateAsset"], Literal["ListRevisionAssets"], Literal["DeleteAsset"], Literal["StartJob"], Literal["SendDataSetNotification"], Literal["UpdateRevision"], Literal["DeleteEventAction"], Literal["ListDataSetRevisions"], Literal["ListDataSets"], Literal["DeleteRevision"], Literal["SendApiAsset"], Literal["CreateEventAction"], Literal["UpdateEventAction"], Literal["ListTagsForResource"], Literal["UpdateAsset"], Literal["PublishDataSet"], Literal["GetEventAction"], Literal["ListEventActions"], Literal["CreateJob"], Literal["CreateDataSet"], Literal["GetRevision"], Literal["GetAsset"], Literal["CancelJob"], Literal["DeleteDataSet"], Literal["UpdateDataSet"], Literal["RevokeRevision"], Literal["ListJobs"], Literal["TagResource"], Literal["CreateRevision"], Literal["GetJob"]]
aws_dataexchange_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_dataexchangeStatement(GenericResourceType[aws_dataexchange_privilege_type, aws_dataexchange_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    