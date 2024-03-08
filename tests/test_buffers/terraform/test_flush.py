from pathlib import Path
from uuid import uuid4

import boto3
import pytest
import shutil
from botocore.exceptions import ClientError

from hangar_sdk.core.terraform import (
    ResourceGroup,
    TerraformBuffer,
    TerraformStateManager
)
from hangar_sdk.resources.terraform.aws.aws_s3_bucket import AwsS3Bucket

basepath = ".hangar"


def bucket_exists(bucket_name):
    s3 = boto3.client("s3")

    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        # The bucket does not exist or you have no access.
        return False


@pytest.fixture(scope="session", autouse=True)
def file_setup():

    # Will be executed before the first test

    yield None

    # Will be executed after the last test

    dothangar = Path(basepath)

    # delete dothangar path recursively

    print("Tearing down environment")
    shutil.rmtree(dothangar)


def test_flush():
    resource_name = "this-is-a-test-hangar-bucket"
    bucket_name = "hangare2etesttf" + str(uuid4()).lower()
    group = ResourceGroup(name="hello", region="us-west-1")
    bucket = AwsS3Bucket(top_name=resource_name, group=group, bucket=bucket_name)

    tf_buffer = group.buffer

    tf_buffer.add(bucket)
    tf_buffer.flush(bucket.get_name())

    wanted_path = Path(basepath) / "hello" / f"{resource_name}.tf"

    assert wanted_path.exists() is True
    assert bucket_exists(bucket_name) is True

    state_manager = TerraformStateManager()

    tf_buffer.load()

    assert bucket_exists(bucket_name) is True
    assert bucket.get_state() is not None
    assert bucket.get_state()["values"]["bucket"] == bucket_name

    tf_buffer.destroy()
    tf_buffer.load()

    assert wanted_path.exists() is True
    assert bucket_exists(bucket_name) is False
    assert bucket.get_state() is None
