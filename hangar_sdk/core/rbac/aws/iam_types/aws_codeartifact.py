from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codeartifact_privilege_type = Union[Literal["PublishPackageVersion"], Literal["DescribeDomain"], Literal["ListDomains"], Literal["UntagResource"], Literal["DisassociateExternalConnection"], Literal["ListPackageVersionAssets"], Literal["ListPackageVersionDependencies"], Literal["GetAuthorizationToken"], Literal["GetPackageVersionAsset"], Literal["DescribePackageVersion"], Literal["ListPackageVersions"], Literal["CreateRepository"], Literal["ReadFromRepository"], Literal["GetRepositoryEndpoint"], Literal["UpdateRepository"], Literal["AssociateExternalConnection"], Literal["CopyPackageVersions"], Literal["ListRepositories"], Literal["UpdatePackageVersionsStatus"], Literal["CreateDomain"], Literal["ListTagsForResource"], Literal["DeletePackage"], Literal["DeleteRepositoryPermissionsPolicy"], Literal["DeleteDomainPermissionsPolicy"], Literal["GetRepositoryPermissionsPolicy"], Literal["ListPackages"], Literal["GetDomainPermissionsPolicy"], Literal["DescribeRepository"], Literal["PutPackageOriginConfiguration"], Literal["PutRepositoryPermissionsPolicy"], Literal["PutDomainPermissionsPolicy"], Literal["DescribePackage"], Literal["DeletePackageVersions"], Literal["ListRepositoriesInDomain"], Literal["DeleteDomain"], Literal["TagResource"], Literal["GetPackageVersionReadme"], Literal["DeleteRepository"], Literal["DisposePackageVersions"], Literal["PutPackageMetadata"], Literal["AssociateWithDownstreamRepository"]]
aws_codeartifact_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codeartifactStatement(GenericResourceType[aws_codeartifact_privilege_type, aws_codeartifact_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    