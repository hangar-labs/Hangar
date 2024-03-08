from pathlib import Path
from uuid import uuid4

import boto3
import pytest
import shutil
from botocore.exceptions import ClientError

from hangar_sdk.core.terraform import ResourceGroup, TerraformBuffer
from hangar_sdk.core.blocks.aws_blocks import AwsBucket

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


def test_s3():
    resource_name = "test-hangar-bucket-" + str(uuid4()).lower()

    group = ResourceGroup(name="hello", region="us-west-1")

    bucket = AwsBucket(name=resource_name, group=group)

    group.resolve()

    wanted_path = Path(basepath) / "hello" / f"{resource_name}.tf"

    assert wanted_path.exists() == True
    assert bucket_exists(resource_name) == True
    assert bucket.bucket.get_state() != None
    assert bucket.bucket.get_state()["values"]["bucket"] == resource_name

    group.buffer.destroy()
    group.buffer.load()

    assert wanted_path.exists() == True
    assert bucket_exists(resource_name) == False
    assert bucket.bucket.get_state() == None
