import json
import subprocess
from pathlib import Path
from typing import Dict, Literal, Sequence, Union

from attrs import Factory, define, field

from hangar_sdk.core import ExecutionType, IBuffer, IResource, IStateManager
from hangar_sdk.core.utils import execute_command


@define(kw_only=True)
class TerraformStateManager(IStateManager):
    state: dict = field(default=Factory(dict))

    def get_state(self, key):
        if "values" not in self.state:
            return None

        resources = self.state["values"]["root_module"]["resources"]
        for r in resources:
            if r["name"] == key:
                return r

        return None

    def set_state(self, state):
        self.state = state


@define(kw_only=True)
class TerraformBuffer(IBuffer):
    basepath: str
    state_manager: Union[TerraformStateManager, None] = None
    initflags: list = field(default=Factory(list))
    applyflags: list = field(default=Factory(list))
    env: dict = field(default=Factory(dict))
    executable: str = "terraform"
    resources: Dict[str, IResource] = field(default=Factory(dict))
    mode: Union[Literal["apply"], Literal["destroy"], Literal["plan"]] = "apply"
    group_name: str
    initialized: bool = False

    def __post_init__(self, **kwargs):
        if self.state_manager is None:
            self.state_manager = TerraformStateManager()

        self.initialized = False

    @property
    def path(self):
        # if self.group_name is None:
        #     raise Exception("Buffer has no resource group. Cannot retrieve path.")
        return Path(self.basepath) / self.group_name

    def add(self, resource: IResource):
        self.resources[resource.get_name()] = resource

    def add_list(self, resources: Sequence[IResource]):
        for resource in resources:
            self.add(resource)

    def write(self):
        self.path.mkdir(parents=True, exist_ok=True)

        for _, resource in self.resources.items():

            with self.path.joinpath(f"{resource.get_name()}.tf").open("w") as f:
                f.write("\n")
                f.write(resource.resolve())
                f.write("\n")

    def flush(self, name, type: ExecutionType = "create"):
        self.write()
        if name not in self.resources:
            raise ValueError(f"Resource {name} not found in buffer")

        resource = self.resources[name]

        self.applyflags = [
            f"-target={resource.get_type()}.{resource.get_name()} -compact-warnings"
        ]

        if type == "create":
            self.apply()
        elif type == "delete":
            self.destroy()
        elif type == "plan":
            self.plan()
        elif type == "act":
            pass
        else:
            raise ValueError(f"Invalid mode {type}")

    def flush_all(self, type: ExecutionType = "create"):
        self.write()

        if type == "create":
            self.apply()
        elif type == "delete":
            self.destroy()
        elif type == "plan":
            self.plan()
        elif type == "act":
            pass
        else:
            raise ValueError(f"Invalid mode {type}")

    def init(self):
        returncode, stdout, stderr = execute_command(
            f"{self.executable} init {' '.join(self.initflags)}",
            env=self.env,
            path=self.path,
        )

        if returncode != 0:
            raise Exception(f"Error initializing terraform: {stderr}")
        self.initialized = True
        return returncode, stdout, stderr

    def apply(self):
        if not self.initialized:
            self.init()

        returncode, stdout, stderr = execute_command(
            f"{self.executable} apply -auto-approve {' '.join(self.applyflags)}",
            env=self.env,
            path=self.path,
        )

        if returncode != 0:
            raise Exception(f"Error applying terraform: {stderr}")

        return returncode, stdout, stderr

    def destroy(self):
        if not self.initialized:
            self.init()

        returncode, stdout, stderr = execute_command(
            f"{self.executable} destroy -auto-approve {' '.join(self.applyflags)}",
            env=self.env,
            path=self.path,
        )

        if returncode != 0:
            raise Exception(f"Error destroying terraform: {stderr}")

        return returncode, stdout, stderr

    def plan(self):
        if not self.initialized:
            self.init()

        returncode, stdout, stderr = execute_command(
            f"{self.executable} plan -auto-approve {' '.join(self.applyflags)}",
            env=self.env,
            path=self.path,
        )

        if returncode != 0:
            raise Exception(f"Error planning terraform: {stderr}")

        return returncode, stdout, stderr

    def load(self):
        if self.state_manager is None:
            raise Exception("No state manager found on buffer")

        process = subprocess.run(
            f"{self.executable} show -json",
            cwd=self.path,
            env=self.env,
            shell=True,
            capture_output=True,
            text=True,
        )
        returncode, stdout, stderr = process.returncode, process.stdout, process.stderr
        if returncode != 0:
            raise Exception(f"Error loading terraform: {stderr}")

        state = stdout

        if state:
            state_json = json.loads(state)
            self.state_manager.set_state(state_json)

        return returncode, stdout, stderr
