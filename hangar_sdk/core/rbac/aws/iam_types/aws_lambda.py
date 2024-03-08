from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_lambda_privilege_type = Union[Literal["GetRuntimeManagementConfig"], Literal["InvokeFunction"], Literal["CreateFunctionUrlConfig"], Literal["UntagResource"], Literal["GetLayerVersion"], Literal["GetFunction"], Literal["GetFunctionUrlConfig"], Literal["CreateFunction"], Literal["ListCodeSigningConfigs"], Literal["ListTags"], Literal["GetFunctionConcurrency"], Literal["DeleteFunctionEventInvokeConfig"], Literal["CreateCodeSigningConfig"], Literal["InvokeAsync"], Literal["ListVersionsByFunction"], Literal["RemovePermission"], Literal["DeleteAlias"], Literal["DeleteLayerVersion"], Literal["GetFunctionConfiguration"], Literal["ListFunctions"], Literal["GetProvisionedConcurrencyConfig"], Literal["ListProvisionedConcurrencyConfigs"], Literal["PublishVersion"], Literal["PutProvisionedConcurrencyConfig"], Literal["GetFunctionCodeSigningConfig"], Literal["GetCodeSigningConfig"], Literal["DeleteCodeSigningConfig"], Literal["ListLayerVersions"], Literal["GetAccountSettings"], Literal["PutFunctionCodeSigningConfig"], Literal["UpdateFunctionUrlConfig"], Literal["UpdateCodeSigningConfig"], Literal["EnableReplication"], Literal["DeleteProvisionedConcurrencyConfig"], Literal["CreateEventSourceMapping"], Literal["RemoveLayerVersionPermission"], Literal["DeleteFunction"], Literal["PutFunctionEventInvokeConfig"], Literal["ListFunctionEventInvokeConfigs"], Literal["DeleteFunctionConcurrency"], Literal["ListEventSourceMappings"], Literal["UpdateAlias"], Literal["UpdateEventSourceMapping"], Literal["UpdateFunctionConfiguration"], Literal["GetLayerVersionPolicy"], Literal["CreateAlias"], Literal["GetPolicy"], Literal["UpdateFunctionCode"], Literal["InvokeFunctionUrl"], Literal["ListFunctionsByCodeSigningConfig"], Literal["AddPermission"], Literal["UpdateFunctionEventInvokeConfig"], Literal["PutRuntimeManagementConfig"], Literal["GetFunctionEventInvokeConfig"], Literal["DeleteFunctionCodeSigningConfig"], Literal["TagResource"], Literal["GetAlias"], Literal["ListAliases"], Literal["AddLayerVersionPermission"], Literal["PublishLayerVersion"], Literal["PutFunctionConcurrency"], Literal["UpdateFunctionCodeSigningConfig"], Literal["ListFunctionUrlConfigs"], Literal["ListLayers"], Literal["DeleteEventSourceMapping"], Literal["GetEventSourceMapping"], Literal["DeleteFunctionUrlConfig"], Literal["DisableReplication"]]
aws_lambda_condition_type = Union[Literal["aws:TagKeys"], Literal["lambda:CodeSigningConfigArn"], Literal["lambda:VpcIds"], Literal["lambda:Principal"], Literal["lambda:EventSourceToken"], Literal["lambda:SecurityGroupIds"], Literal["aws:RequestTag/${TagKey}"], Literal["lambda:FunctionUrlAuthType"], Literal["lambda:Layer"], Literal["lambda:SubnetIds"], Literal["lambda:FunctionArn"]]

class aws_lambdaStatement(GenericResourceType[aws_lambda_privilege_type, aws_lambda_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    