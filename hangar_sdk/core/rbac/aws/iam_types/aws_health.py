from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_health_privilege_type = Union[Literal["DescribeEntityAggregatesForOrganization"], Literal["DescribeEventTypes"], Literal["DescribeEntityAggregates"], Literal["DescribeEventsForOrganization"], Literal["DescribeEventDetails"], Literal["DescribeAffectedEntities"], Literal["DescribeEvents"], Literal["DescribeHealthServiceStatusForOrganization"], Literal["DisableHealthServiceAccessForOrganization"], Literal["EnableHealthServiceAccessForOrganization"], Literal["DescribeAffectedEntitiesForOrganization"], Literal["DescribeEventDetailsForOrganization"], Literal["DescribeEventAggregates"], Literal["DescribeAffectedAccountsForOrganization"]]
aws_health_condition_type = Union[Literal["health:eventTypeCode"], Literal["health:service"]]

class aws_healthStatement(GenericResourceType[aws_health_privilege_type, aws_health_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    