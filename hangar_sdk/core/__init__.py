from abc import ABC, abstractmethod
from typing import Any, Literal, Optional, Union

from typing_extensions import Sequence

ExecutionType = Union[
    Literal["create"], Literal["delete"], Literal["act"], Literal["plan"]
]


class IResource(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def resolve(self, type: ExecutionType = "create") -> Any:
        pass

    @abstractmethod
    def get_state(self) -> Optional[dict]:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass


class IGroup(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_buffer(self) -> "IBuffer":
        pass

    @abstractmethod
    def get_state_manager(self) -> "IStateManager":
        pass


class IStateManager(ABC):
    @abstractmethod
    def get_state(self, key: str) -> Optional[dict]:
        pass


class IBuffer(ABC):
    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def flush_all(self, mode):
        pass

    @abstractmethod
    def flush(self, name, mode):
        pass

    @abstractmethod
    def load(self, type: ExecutionType = "create") -> Any:
        pass

    @abstractmethod
    def add(self, resource: IResource):
        pass

    def add_list(self, resources: Sequence[IResource]):
        for resource in resources:
            self.add(resource)
