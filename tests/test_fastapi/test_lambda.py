import asyncio
import json
import os
import uuid

from hangar_sdk.core.blocks.aws_blocks import AwsBucket
from hangar_sdk.core.terraform import ResourceGroup
from hangar_sdk.serverless import ServerlessApp

from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    hangar_scope = ResourceGroup(name="func-scope", region="us-west-1", terraform_executable="/opt/homebrew/bin/terraform")
    bucket_name = "test-func-bucket-hangar-langserve"
    lambda_app = ServerlessApp(
        name="serverless-test",
        group=hangar_scope,
        project_path=os.getcwd(),
        role_arn=os.getenv("HANGAR_LAMBDA_TEST_ROLE"),
        bucket=AwsBucket(group=hangar_scope, name=bucket_name),
    )
    lambda_app.FastApi(func=handler, app_file_name="test_lambda.py", timeout=60 * 2, environment_variables={"test": "test"})
    
    asyncio.run(lambda_app.resolve())