from abc import ABCMeta, abstractmethod
from typing import Union


class CP_CYBOS(metaclass=ABCMeta):
    @property
    def IsConnect() -> bool:
        pass
