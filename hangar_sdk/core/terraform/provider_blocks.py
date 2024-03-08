from typing import Optional, Sequence

from attrs import Factory, define, field

from hangar_sdk.core import ExecutionType, IGroup, IResource
from hangar_sdk.resources.terraform.aws import Aws, DefaultTags

@define(kw_only=True, slots=False)
class AwsProvider(IResource):
    name: str
    region: str
    group: IGroup
    _dependencies: list = field(default=Factory(list))
    _resolved: bool = False

    def get_state(self) -> Optional[dict]:
        return {}

    def get_type(self) -> str:
        return ""

    def get_name(self) -> str:
        return self.name

    def _resolve(self, type: ExecutionType = "create"):
        self.aws = Aws(
            top_name="aws_provider",
            region=self.region,
            group=self.group,
            default_tags=[
                DefaultTags(
                    group=self.group,
                    tags={
                        "Environment": "production",
                        "ManagedBy": "hangar",
                    },
                )
            ],
        )

        return [self.aws]

    def _pre_resolve(self):
        pass

    def _post_resolve(
        self, res: Sequence[IResource], type: ExecutionType = "create"
    ) -> Sequence[IResource]:
        for resource in res:
            self.group.get_buffer().add(resource)
            self.group.get_buffer().write()

        return res

    def resolve(self, type: ExecutionType = "create") -> Sequence[IResource]:
        if self._resolved:
            return []

        for resource in self._dependencies:
            resource.resolve(type=type)

        self._pre_resolve()

        res: Sequence[IResource] = self._resolve()

        res = self._post_resolve(res, type)

        self._resolved = True

        return res

