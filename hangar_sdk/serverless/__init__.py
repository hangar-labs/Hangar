import asyncio
import inspect
import json
import os
from typing import Any, Dict, List

from attr import Factory, define, field

from hangar_sdk.core import ExecutionType, IResource
from hangar_sdk.core.blocks.aws_blocks import (
    ArchiveAsset,
    AwsBucket,
    LambdaFunction,
    LambdaLayer,
)
from hangar_sdk.core.terraform import Resource, ResourceGroup
from hangar_sdk.serverless.packager import (
    AppOnlyDeploymentPackager,
    DependencyBuilder,
    LayerDeploymentPackager,
)
from hangar_sdk.serverless.utils import UI, OSUtils, get_current_runtime


@define(frozen=False, slots=False, kw_only=True)
class HangarLambdaPackager(Resource):
    dir_path: str
    runtime: str
    layer: str = ""
    only_app: str = ""
    requirenments_file: str = "requirements.txt"
    group: ResourceGroup

    def _resolve(self, type: ExecutionType = "create"):
        dep_builder = DependencyBuilder(
            osutils=OSUtils(),
        )

        layer_packager = LayerDeploymentPackager(
            osutils=OSUtils(), dependency_builder=dep_builder, ui=UI()
        )

        app_packager = AppOnlyDeploymentPackager(
            osutils=OSUtils(), dependency_builder=dep_builder, ui=UI()
        )

        layer = layer_packager.create_deployment_package(
            project_dir=self.dir_path,
            python_version=self.runtime,
            requirements_filename=self.requirenments_file,
        )

        only_app = app_packager.create_deployment_package(
            project_dir=self.dir_path, python_version=self.runtime
        )

        if type == "delete":
            try:
                os.remove(layer)
                os.remove(only_app)
            except FileNotFoundError:
                pass
            return

        self.layer = layer
        self.only_app = only_app

        return []


class HangarServerlessFunction:
    def __init__(self, func, group: ResourceGroup, secrets: Dict[str, str] = {}):
        self.func = func
        self.group = group
        self.secrets = secrets

    def __call__(self, event, context) -> Any:
        args = event.get("args", [])
        kwargs = event.get("kwargs", {})

        sig = inspect.signature(self.func)
        if "event" in sig.parameters:
            kwargs["event"] = event

        if "context" in sig.parameters:
            kwargs["context"] = context

        for key, value in self.secrets.items():
            session = self.group.get_session()
            print(session.client("ssm").get_parameter(Name=value, WithDecryption=True))
            value = session.client("ssm").get_parameter(
                Name=value, WithDecryption=True
            )["Parameter"]["Value"]
            os.environ[key] = value
            print(f"Setting {key} to {value}")

        return self.func(*args, **kwargs)

    def invoke(self, *args, **kwargs):
        payload = {"args": args, "kwargs": kwargs}

        client = self.group.get_session().client("lambda")

        response = client.invoke(
            FunctionName=self.func.__name__,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload),
        )
        return json.loads(response["Payload"].read().decode("utf-8"))


class LocalHangarServerlessFunction:
    def __init__(self, func, group) -> None:
        self.func = func
        self.group = group

    def __call__(self, *args, **kwargs) -> Any:
        if os.getenv("HANGAR_ENVIRONMENT") == "LOCAL":
            payload = {"args": args, "kwargs": kwargs}
            client = self.group.get_session().client("lambda")

            response = client.invoke(
                FunctionName=self.func.__name__,
                InvocationType="RequestResponse",
                Payload=json.dumps(payload),
            )
            return json.loads(response["Payload"].read().decode("utf-8"))

        else:
            raise Exception(
                "Cannot call remote function. Call within a local function."
            )

    def invoke(self, *args, **kwargs):
        return self(*args, **kwargs)


@define(slots=False, kw_only=True)
class ServerlessApp:
    path: str = field(default=os.getcwd())
    name: str
    project_path: str
    local_entrypoint: Any = None
    bucket: AwsBucket
    group: ResourceGroup
    role_arn: str
    requirenments_file: str = "requirements.txt"
    _functions: list = field(default=Factory(list))
    mode: str = "deploy"

    @property
    def env(self):
        return os.getenv("HANGAR_ENVIRONMENT")

    def Function(self, timeout=60, environment_variables={}, role=None, secrets={}):
        def function_decorator(func):
            if self.env == "REMOTE":
                print("Remote")
                return HangarServerlessFunction(func, self.group, secrets=secrets)

            if self.env == "LOCAL":
                return LocalHangarServerlessFunction(func, self.group, secrets=secrets)
            else:
                functionPath = (
                    os.path.basename(inspect.getfile(func)).split(".")[0]
                    + "."
                    + func.__name__
                )

                self._functions.append(
                    {
                        "path": functionPath,
                        "timeout": timeout,
                        "environment_variables": environment_variables,
                        "role": role,
                    }
                )
                return LocalHangarServerlessFunction(func, self.group)

        return function_decorator

    def FastApi(self, func, app_file_name, timeout=60, environment_variables={}, role=None, secrets={}):
       
        if self.env == "REMOTE":
            print("Remote")
            return HangarServerlessFunction(func, self.group, secrets=secrets)

        if self.env == "LOCAL":
            return LocalHangarServerlessFunction(func, self.group, secrets=secrets)
        else:
            functionPath = (
                os.path.basename(os.path.join(self.project_path, app_file_name)).split(".")[0]
                + "."
                + "handler"
            )

            self._functions.append(
                {
                    "path": functionPath,
                    "timeout": timeout,
                    "environment_variables": environment_variables,
                    "role": role,
                }
            )
            return LocalHangarServerlessFunction(func, self.group)

    def LocalEntrypoint(self, func):
        self.local_function = func
        return

    def deploy(self):
        return asyncio.run(self.resolve())

    def destroy(self):
        return asyncio.run(self.resolve(type="delete"))

    def plan(self):
        return asyncio.run(self.resolve(type="plan"))

    def act(self):
        return asyncio.run(self.resolve(type="act"))

    async def resolve(self, type: ExecutionType = "create"):
        if self.env == "REMOTE":
            return

        if self.mode == "act":
            if self.local_function:
                os.environ["HANGAR_ENVIRONMENT"] = "LOCAL"
                self.local_function()
                del os.environ["HANGAR_ENVIRONMENT"]

            return

        current_runtime = get_current_runtime()

        packager = HangarLambdaPackager(
            group=self.group,
            dir_path=self.project_path,
            runtime=current_runtime,
            name="hangar_serverless_packager",
            requirenments_file=self.requirenments_file,
        )

        packager._resolve()

        self._resources: List[IResource] = []

        asset_bucket = self.bucket

        layer_asset = ArchiveAsset(
            name=self.name + "-hangar_serverless_layer_asset",
            path=packager.layer,
            bucket=asset_bucket,
            group=self.group,
        )

        app_asset = ArchiveAsset(
            name=self.name + "-hangar-serverless-app-asset",
            path=packager.only_app,
            bucket=asset_bucket,
            group=self.group,
        )

        layer = LambdaLayer(
            group=self.group,
            name=self.name + "-hangar_serverless_layer",
            asset=layer_asset,
            runtimes=[current_runtime],
        )

        print(self._functions)
        print("RESOLVING FUNCTIONS")

        for func in self._functions:
            LambdaFunction(
                group=self.group,
                name="hangar_serverless_" + func["path"].split(".")[1],
                handler=func["path"],
                asset=app_asset,
                function_name=func["path"].split(".")[1],
                role=self.role_arn if func["role"] is None else func["role"],
                runtime=current_runtime,
                timeout=func["timeout"],
                environment={
                    "HANGAR_ENVIRONMENT": "REMOTE",
                    **func["environment_variables"],
                },
                layers=[layer],
            )

        self.group.resolve(type=type)

        return self._resources
