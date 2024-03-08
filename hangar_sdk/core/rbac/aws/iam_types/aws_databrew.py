from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_databrew_privilege_type = Union[Literal["CreateProject"], Literal["UntagResource"], Literal["UpdateProfileJob"], Literal["ListSchedules"], Literal["UpdateRecipe"], Literal["DescribeDataset"], Literal["DeleteJob"], Literal["DeleteRuleset"], Literal["CreateRecipe"], Literal["DescribeRecipe"], Literal["DeleteRecipeVersion"], Literal["StartJobRun"], Literal["CreateDataset"], Literal["CreateSchedule"], Literal["ListTagsForResource"], Literal["ListProjects"], Literal["StopJobRun"], Literal["ListRulesets"], Literal["UpdateSchedule"], Literal["UpdateDataset"], Literal["ListRecipeVersions"], Literal["UpdateProject"], Literal["BatchDeleteRecipeVersion"], Literal["ListRecipes"], Literal["CreateRuleset"], Literal["DescribeSchedule"], Literal["CreateRecipeJob"], Literal["DescribeJobRun"], Literal["DescribeRuleset"], Literal["ListJobRuns"], Literal["DeleteProject"], Literal["PublishRecipe"], Literal["StartProjectSession"], Literal["ListDatasets"], Literal["UpdateRecipeJob"], Literal["DescribeProject"], Literal["ListJobs"], Literal["TagResource"], Literal["SendProjectSessionAction"], Literal["CreateProfileJob"], Literal["DeleteDataset"], Literal["DeleteSchedule"], Literal["UpdateRuleset"], Literal["DescribeJob"]]
aws_databrew_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_databrewStatement(GenericResourceType[aws_databrew_privilege_type, aws_databrew_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    