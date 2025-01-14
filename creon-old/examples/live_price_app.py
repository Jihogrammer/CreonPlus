from typing import TYPE_CHECKING

from creon.models import EventHandler
from creon.models.live_price import LivePrice
from creon.utils.creon_api import bind_module_with_eventhandler, get_stock_cur_module


if TYPE_CHECKING:
    from models import Module


class MyHandler(EventHandler):
    def init(self, module: "Module") -> None:
        self.__module = module

    def subscribe(self) -> None:
        self.__module.Subscribe()

    def unsubscribe(self) -> None:
        self.__module.Unsubscribe()

    def OnReceived(self) -> None:
        dto = LivePrice(
            self.__module.GetHeaderValue(0),
            self.__module.GetHeaderValue(1),
            self.__module.GetHeaderValue(13),
            self.__module.GetHeaderValue(18),
        )
        print(dto)


class Subscriber:
    __module: "Module"

    def __init__(self):
        self.__module = get_stock_cur_module()
        self.__module.SetInputValue(0, "A005930")
        self.__handler = bind_module_with_eventhandler(self.__module, MyHandler)
        self.__handler.init(self.__module)

    def subscribe(self):
        self.__handler.subscribe()


def example():
    import pythoncom

    print("\033[1;33mExample live price subscribe.\033[0m")
    Subscriber().subscribe()
    while True:
        pythoncom.PumpWaitingMessages()
