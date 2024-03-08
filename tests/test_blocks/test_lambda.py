import os

from hangar_sdk.core.blocks.aws_blocks import (
    ArchiveAsset,
    AwsBucket,
    LambdaFunction
)
from hangar_sdk.core.terraform import ResourceGroup


def test_lambda():
    hangar_group = ResourceGroup(
        name="hangar",
    )

    asset_path = os.path.dirname(os.path.abspath(__file__)) + "/lambda_function.zip"

    assert os.path.exists(asset_path)

    func = LambdaFunction(
        name="hangar",
        group=hangar_group,
        handler="lambda_function/lambda_handler.lambda_handler",
        runtime="python3.10",
        asset=ArchiveAsset(
            name="lambda_asset",
            bucket=AwsBucket(
                name="hangar-lambda-assets",
                group=hangar_group,
            ),
            path=asset_path,
            group=hangar_group,
        ),
        timeout=10,
        environment={"key": "value"},
        role=os.getenv("HANGAR_LAMBDA_TEST_ROLE"),
    )

    assert hangar_group.get_resources() == [func.asset.bucket, func.asset, func]

    hangar_group.resolve()

    assert (
        func.state["aws_lambda_function"]["hangar"]["values"]["function_name"]
        == "hangar"
    )

    assert (
        func.state["aws_lambda_function"]["hangar"]["values"]["handler"]
        == "lambda_function/lambda_handler.lambda_handler"
    )

    assert func.invoke(payload={"key": "value"}) == "Hello, world!"
