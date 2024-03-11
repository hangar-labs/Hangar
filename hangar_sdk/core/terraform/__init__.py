from abc import ABC, abstractmethod
from typing import List, Optional, Sequence

import boto3
from attr import Factory, define, field

from hangar_sdk.core import ExecutionType, IBuffer, IGroup, IResource, IStateManager
from hangar_sdk.core.terraform.buffer import TerraformBuffer, TerraformStateManager
from hangar_sdk.core.terraform.provider_blocks import AwsProvider


@define(kw_only=True)
class ResourceGroup(IGroup):
    name: str
    region: str
    resources: List["Resource"] = field(default=Factory(list))
    state_manager: Optional[TerraformStateManager] = None
    buffer: Optional[TerraformBuffer] = None
    terraform_excecutable: str = "terraform"

    def __attrs_post_init__(self):
        self.state_manager = TerraformStateManager()
        self.buffer = TerraformBuffer(
            basepath=".hangar",
            state_manager=self.state_manager,
            group_name=self.get_name(),
            executable=self.terraform_excecutable,
        )

        self.aws_config = AwsProvider(
            name="aws",
            region=self.region,
            group=self,
        )

    def get_buffer(self) -> IBuffer:
        if self.buffer is None:
            raise ValueError(f"Group {self.get_name()} `buffer` is None, Aborting")
        return self.buffer

    def get_state_manager(self) -> IStateManager:
        if self.state_manager is None:
            raise ValueError(
                f"Group {self.get_name()} `state_manager` is None, Aborting"
            )
        return self.state_manager

    def get_name(self) -> str:
        return self.name

    def resolve(self, type: ExecutionType = "create"):
        resources = [self.aws_config]
        resources += self.resources

        base_resources: List[IResource] = []

        while len(resources) != 0:
            resource = resources.pop(0)

            if isinstance(resource, Resource) or isinstance(resource, AwsProvider):
                sub_resources = resource.resolve(type=type)
                base_resources += sub_resources
            else:
                base_resources += resource
        if self.buffer is None:
            raise ValueError(f"Group {self.get_name()} `buffer` is None, Aborting")
        self.buffer.load()

    def get_resources(self) -> Sequence[IResource]:
        return self.resources

    def add_resource(self, resource: "Resource"):
        self.resources.append(resource)

    def get_session(self):
        return boto3.session.Session(
            region_name=self.region,
        )


@define(kw_only=True, slots=False)
class Resource(IResource, ABC):
    name: str
    group: ResourceGroup
    _dependencies: list = field(default=Factory(list))
    _resolved: bool = False

    def __attrs_post_init__(self):
        # if a field is a type of L1ResourceBase, add it to the dependencies list
        for k, f in self.__dict__.items():
            if k.startswith("_"):
                continue
            if isinstance(f, Resource):
                self._dependencies.append(f)

            elif isinstance(f, list):
                for item in f:
                    if isinstance(item, Resource):
                        self._dependencies.append(item)

        self.group.add_resource(self)

    def get_name(self) -> str:
        return self.name

    def get_type(self):
        return self.__class__.__name__

    def _pre_resolve(self):
        pass

    @abstractmethod
    def _resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        pass

    def _post_resolve(
        self, res: Sequence[IResource], type: ExecutionType = "create"
    ) -> Sequence[IResource]:
        for resource in res:
            if isinstance(resource, Resource):
                raise ValueError(f"Resource {resource} is not a valid resource")

            if self.group.buffer is None:
                raise ValueError(
                    f"Group {self.group.get_name()} `buffer` is None, Aborting"
                )

            self.group.buffer.add(resource)
            print(f"Adding {resource.get_name()} to buffer")
            self.group.buffer.flush(resource.get_name(), type=type)

        return res

    def resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        if self._resolved:
            return []

        for resource in self._dependencies:
            resource.resolve(type=type)

        self._pre_resolve()

        res: Sequence[IResource] = self._resolve(type=type)

        res = self._post_resolve(res, type)

        self._resolved = True

        return res

    def get_group(self):
        return self.group

    @property
    def state(self):
        return self.get_state()

    def get_state(self) -> Optional[dict]:
        res: dict = {}

        if self.group.state_manager is None:
            raise ValueError(
                f"Group {self.group.get_name()} `state_manager` is None, Aborting"
            )

        for resource in self._resolve():
            rtype = resource.get_type()
            rname = resource.get_name()

            if rtype not in res:
                res[rtype] = {}

            res[rtype][rname] = self.group.state_manager.get_state(rname)

        return res
