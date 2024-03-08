from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_entityresolution_privilege_type = Union[Literal["DeleteMatchingWorkflow"], Literal["UntagResource"], Literal["ListIdMappingWorkflows"], Literal["GetMatchingJob"], Literal["UpdateIdMappingWorkflow"], Literal["GetProviderService"], Literal["DeleteIdMappingWorkflow"], Literal["CreateIdMappingWorkflow"], Literal["ListSchemaMappings"], Literal["CreateSchemaMapping"], Literal["ListTagsForResource"], Literal["GetIdMappingWorkflow"], Literal["StartMatchingJob"], Literal["ListMatchingWorkflows"], Literal["ListIdMappingJobs"], Literal["DeleteSchemaMapping"], Literal["GetMatchingWorkflow"], Literal["ListMatchingJobs"], Literal["GetIdMappingJob"], Literal["StartIdMappingJob"], Literal["TagResource"], Literal["UpdateSchemaMapping"], Literal["UpdateMatchingWorkflow"], Literal["GetMatchId"], Literal["ListProviderServices"], Literal["CreateMatchingWorkflow"], Literal["GetSchemaMapping"]]
aws_entityresolution_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_entityresolutionStatement(GenericResourceType[aws_entityresolution_privilege_type, aws_entityresolution_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    