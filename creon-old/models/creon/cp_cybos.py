from abc import ABCMeta


class CP_CYBOS(metaclass=ABCMeta):
    @property
    def IsConnect() -> bool:
        pass
