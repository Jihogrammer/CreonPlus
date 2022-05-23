from abc import ABCMeta, abstractmethod
from typing import Union


class BaseModule(metaclass=ABCMeta):
    """Creon Plus Cybos Base Module"""

    @abstractmethod
    def GetHeaderValue(self, type: int) -> Union[int, str, float]:
        raise Exception("구현되지 않은 메서드입니다.")

    @abstractmethod
    def SetInputValue(self, type: int, code: str):
        raise Exception("구현되지 않은 메서드입니다.")

    @abstractmethod
    def Subscribe(self):
        raise Exception("구현되지 않은 메서드입니다.")

    @abstractmethod
    def Unsubscribe(self):
        raise Exception("구현되지 않은 메서드입니다.")
