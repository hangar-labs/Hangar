import json
import os
import uuid

import boto3
import pytest

from hangar_sdk.core.blocks.aws_blocks import AwsBucket
from hangar_sdk.core.terraform import ResourceGroup
from hangar_sdk.serverless import ServerlessApp

hangar_scope = ResourceGroup(name="func-scope", region="us-west-1")

bucket_name = "test-func-bucket-hangar" + uuid.uuid4().hex[:6].lower()

app = ServerlessApp(
    name="serverless-test",
    group=hangar_scope,
    project_path=os.getcwd(),
    role_arn=os.getenv("HANGAR_LAMBDA_TEST_ROLE"),
    bucket=AwsBucket(group=hangar_scope, name=bucket_name),
)

@app.Function(timeout=60 * 2, environment_variables={"test": "test"})
def sdkfunc2():
    import os

    return os.getenv("test")

@app.Function(
    timeout=60 * 2,
    environment_variables={"test": "test"},
    secrets={"test": "test_hangar"},
)
def hangarfunction2(description):

    print(description)
    print(boto3.client("ssm").get_parameter(Name="test_hangar"))
    print(os.getenv("test"))

    return os.getenv("test")

@app.LocalEntrypoint
def local():
    print(hangarfunction2("I love reading about tech"))

@pytest.fixture(scope="session", autouse=True)
def file_setup():
    app.deploy()
    yield None

def test_samsfunction():

    os.environ["HANGAR_ENVIRONMENT"] = "LOCAL"
    assert hangarfunction2("I love reading about tech") == "hello"
