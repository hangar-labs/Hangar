from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2NetworkInsightsAnalysis(AbstractTerraformResource):
    _group: Any
    _top_name: str
    network_insights_path_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_network_insights_analysis")
    filter_in_arns: Optional[Sequence[str]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    wait_for_completion: Optional[bool] = None
