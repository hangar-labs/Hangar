from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_vendor_insights_privilege_type = Union[Literal["UntagResource"], Literal["ListSecurityProfiles"], Literal["UpdateSecurityProfileSnapshotReleaseConfiguration"], Literal["AssociateDataSource"], Literal["ListEntitledSecurityProfileSnapshots"], Literal["UpdateDataSource"], Literal["ActivateSecurityProfile"], Literal["ListSecurityProfileSnapshots"], Literal["UpdateSecurityProfile"], Literal["ListDataSources"], Literal["GetDataSource"], Literal["ListTagsForResource"], Literal["GetEntitledSecurityProfileSnapshot"], Literal["ListEntitledSecurityProfiles"], Literal["GetProfileAccessTerms"], Literal["CreateDataSource"], Literal["GetSecurityProfile"], Literal["DisassociateDataSource"], Literal["DeactivateSecurityProfile"], Literal["UpdateSecurityProfileSnapshotCreationConfiguration"], Literal["TagResource"], Literal["CreateSecurityProfile"], Literal["GetSecurityProfileSnapshot"], Literal["DeleteDataSource"]]
aws_vendor_insights_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_vendor_insightsStatement(GenericResourceType[aws_vendor_insights_privilege_type, aws_vendor_insights_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    