from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_qldb_privilege_type = Union[Literal["GetDigest"], Literal["DescribeJournalKinesisStream"], Literal["CreateLedger"], Literal["UntagResource"], Literal["ListJournalS3Exports"], Literal["PartiQLHistoryFunction"], Literal["DescribeJournalS3Export"], Literal["ListJournalS3ExportsForLedger"], Literal["PartiQLUpdate"], Literal["PartiQLCreateIndex"], Literal["ExportJournalToS3"], Literal["GetBlock"], Literal["PartiQLInsert"], Literal["ExecuteStatement"], Literal["ListTagsForResource"], Literal["PartiQLRedact"], Literal["UpdateLedgerPermissionsMode"], Literal["ShowCatalog"], Literal["PartiQLDropTable"], Literal["PartiQLCreateTable"], Literal["UpdateLedger"], Literal["GetRevision"], Literal["CancelJournalKinesisStream"], Literal["DescribeLedger"], Literal["SendCommand"], Literal["ListLedgers"], Literal["TagResource"], Literal["PartiQLDropIndex"], Literal["InsertSampleData"], Literal["PartiQLUndropTable"], Literal["StreamJournalToKinesis"], Literal["PartiQLDelete"], Literal["PartiQLSelect"], Literal["ListJournalKinesisStreamsForLedger"], Literal["DeleteLedger"]]
aws_qldb_condition_type = Union[Literal["aws:TagKeys"], Literal["qldb:Purge"], Literal["aws:RequestTag/${TagKey}"]]

class aws_qldbStatement(GenericResourceType[aws_qldb_privilege_type, aws_qldb_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    