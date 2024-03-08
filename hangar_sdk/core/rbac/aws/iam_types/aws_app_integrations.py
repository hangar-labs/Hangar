from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_app_integrations_privilege_type = Union[Literal["GetEventIntegration"], Literal["CreateDataIntegration"], Literal["CreateEventIntegration"], Literal["UntagResource"], Literal["CreateEventIntegrationAssociation"], Literal["DeleteDataIntegration"], Literal["ListDataIntegrationAssociations"], Literal["ListEventIntegrationAssociations"], Literal["CreateApplication"], Literal["UpdateApplication"], Literal["UpdateDataIntegration"], Literal["ListTagsForResource"], Literal["CreateDataIntegrationAssociation"], Literal["ListEventIntegrations"], Literal["CreateApplicationAssociation"], Literal["DeleteApplication"], Literal["ListApplicationAssociations"], Literal["ListApplications"], Literal["DeleteEventIntegration"], Literal["DeleteDataIntegrationAssociation"], Literal["UpdateEventIntegration"], Literal["GetApplication"], Literal["TagResource"], Literal["DeleteEventIntegrationAssociation"], Literal["DeleteApplicationAssociation"], Literal["ListDataIntegrations"], Literal["GetDataIntegration"]]
aws_app_integrations_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_app_integrationsStatement(GenericResourceType[aws_app_integrations_privilege_type, aws_app_integrations_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    