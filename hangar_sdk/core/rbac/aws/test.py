from future.iam_gen.base_type import Policy
from future.iam_gen.statement import Statement
from hangar_sdk.core.terraform import ResourceGroup

from hangar_sdk.core.blocks.aws_blocks import AwsBucket

# bucket = AwsBucket
# instance = Instance

# bucket.allows(instance)

# AwsRole.attach(bucket.policy())


def test_basic_resolution():
    p = Policy()

    bucket = AwsBucket(name="hi", group=ResourceGroup(name="hello", region="us-west-2"), tags={})
    bucket.allows(p).withActions(["CreateAccessGrant"]).withPrincipals(["inspector.amazonaws.com", "amplify.amazonaws.com"])

    print(p.escaped_json_policy)


