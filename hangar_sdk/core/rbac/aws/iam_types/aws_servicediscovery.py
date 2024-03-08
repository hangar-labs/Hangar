from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_servicediscovery_privilege_type = Union[Literal["UntagResource"], Literal["GetInstance"], Literal["CreatePublicDnsNamespace"], Literal["UpdatePublicDnsNamespace"], Literal["CreateHttpNamespace"], Literal["UpdateInstanceCustomHealthStatus"], Literal["DeleteService"], Literal["CreateService"], Literal["DiscoverInstances"], Literal["UpdatePrivateDnsNamespace"], Literal["CreatePrivateDnsNamespace"], Literal["GetInstancesHealthStatus"], Literal["ListTagsForResource"], Literal["GetService"], Literal["ListInstances"], Literal["GetOperation"], Literal["UpdateService"], Literal["DeleteNamespace"], Literal["ListOperations"], Literal["ListServices"], Literal["ListNamespaces"], Literal["DiscoverInstancesRevision"], Literal["TagResource"], Literal["RegisterInstance"], Literal["UpdateHttpNamespace"], Literal["GetNamespace"], Literal["DeregisterInstance"]]
aws_servicediscovery_condition_type = Union[Literal["aws:TagKeys"], Literal["servicediscovery:ServiceName"], Literal["servicediscovery:NamespaceArn"], Literal["servicediscovery:ServiceArn"], Literal["servicediscovery:NamespaceName"], Literal["aws:RequestTag/${TagKey}"]]

class aws_servicediscoveryStatement(GenericResourceType[aws_servicediscovery_privilege_type, aws_servicediscovery_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    