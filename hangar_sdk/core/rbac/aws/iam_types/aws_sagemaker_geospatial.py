from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sagemaker_geospatial_privilege_type = Union[Literal["UntagResource"], Literal["DeleteVectorEnrichmentJob"], Literal["DeleteEarthObservationJob"], Literal["ExportVectorEnrichmentJob"], Literal["StartEarthObservationJob"], Literal["StartVectorEnrichmentJob"], Literal["ListTagsForResource"], Literal["GetVectorEnrichmentJob"], Literal["GetEarthObservationJob"], Literal["StopEarthObservationJob"], Literal["ListVectorEnrichmentJobs"], Literal["StopVectorEnrichmentJob"], Literal["ListEarthObservationJobs"], Literal["GetTile"], Literal["GetRasterDataCollection"], Literal["ExportEarthObservationJob"], Literal["TagResource"], Literal["ListRasterDataCollections"], Literal["SearchRasterDataCollection"]]
aws_sagemaker_geospatial_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_sagemaker_geospatialStatement(GenericResourceType[aws_sagemaker_geospatial_privilege_type, aws_sagemaker_geospatial_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    