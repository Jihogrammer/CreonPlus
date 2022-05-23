from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from creon.models.modules import BaseModule


class EventHandler(metaclass=ABCMeta):
    @abstractmethod
    def init(self, module: "BaseModule") -> None:
        pass

    @abstractmethod
    def subscribe(self) -> None:
        pass

    @abstractmethod
    def unsubscribe(self) -> None:
        pass

    @abstractmethod
    def OnReceived(self) -> None:
        pass
