from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_mechanicalturk_privilege_type = Union[Literal["DeleteQualificationType"], Literal["RejectAssignment"], Literal["CreateQualificationType"], Literal["GetHIT"], Literal["ListReviewPolicyResultsForHIT"], Literal["GetAccountBalance"], Literal["DisassociateQualificationFromWorker"], Literal["ListReviewableHITs"], Literal["GetQualificationType"], Literal["CreateHITWithHITType"], Literal["ListBonusPayments"], Literal["UpdateNotificationSettings"], Literal["UpdateHITTypeOfHIT"], Literal["DeleteWorkerBlock"], Literal["RejectQualificationRequest"], Literal["ListQualificationRequests"], Literal["GetQualificationScore"], Literal["ListAssignmentsForHIT"], Literal["NotifyWorkers"], Literal["UpdateExpirationForHIT"], Literal["CreateAdditionalAssignmentsForHIT"], Literal["CreateHITType"], Literal["CreateHIT"], Literal["AcceptQualificationRequest"], Literal["ListWorkersWithQualificationType"], Literal["UpdateHITReviewStatus"], Literal["SendTestEventNotification"], Literal["GetFileUploadURL"], Literal["AssociateQualificationWithWorker"], Literal["UpdateQualificationType"], Literal["DeleteHIT"], Literal["ListHITs"], Literal["ListQualificationTypes"], Literal["ListHITsForQualificationType"], Literal["CreateWorkerBlock"], Literal["ApproveAssignment"], Literal["SendBonus"], Literal["ListWorkerBlocks"], Literal["GetAssignment"]]
aws_mechanicalturk_condition_type = None

class aws_mechanicalturkStatement(GenericResourceType[aws_mechanicalturk_privilege_type, aws_mechanicalturk_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    