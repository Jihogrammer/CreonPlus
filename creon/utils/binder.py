from typing import TYPE_CHECKING, Type

from win32com.client import WithEvents

if TYPE_CHECKING:
    from creon.models.modules import BaseModule
    from creon.models.pubsub import EventHandler


def bind_module_with_eventhandler(
    module: "BaseModule", handler: Type["EventHandler"]
) -> "EventHandler":
    return WithEvents(module, handler)
