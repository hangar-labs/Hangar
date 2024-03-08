from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotroborunner_privilege_type = Union[Literal["UpdateWorkerFleet"], Literal["DeleteWorkerFleet"], Literal["ListDestinations"], Literal["GetDestination"], Literal["UpdateDestination"], Literal["CreateDestination"], Literal["DeleteWorker"], Literal["UpdateSite"], Literal["GetWorkerFleet"], Literal["ListSites"], Literal["UpdateWorker"], Literal["ListWorkers"], Literal["GetSite"], Literal["CreateSite"], Literal["DeleteDestination"], Literal["CreateWorker"], Literal["GetWorker"], Literal["DeleteSite"], Literal["ListWorkerFleets"], Literal["CreateWorkerFleet"]]
aws_iotroborunner_condition_type = None

class aws_iotroborunnerStatement(GenericResourceType[aws_iotroborunner_privilege_type, aws_iotroborunner_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    