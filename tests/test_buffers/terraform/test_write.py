import shutil
from pathlib import Path

import pytest

from hangar_sdk.core.terraform import ResourceGroup, TerraformBuffer
from hangar_sdk.resources.terraform.aws.aws_s3_bucket import AwsS3Bucket

basepath = ".hangar"


@pytest.fixture(scope="session", autouse=True)
def file_setup():

    # Will be executed before the first test

    yield None

    # Will be executed after the last test

    dothangar = Path(basepath)
    shutil.rmtree(dothangar)


def test_write():
    group = ResourceGroup(name="hello", region="us-west-1")

    bucket_name = "this-is-a-test-hangar-bucket"

    bucket = AwsS3Bucket(
        top_name=bucket_name,
        group=group,
        bucket_prefix="something",
    )

    group.buffer.add(bucket)
    assert len(group.buffer.resources) == 1

    group.buffer.write()

    wanted_path = Path(basepath) / "hello" / f"{bucket_name}.tf"

    assert wanted_path.exists() is True
