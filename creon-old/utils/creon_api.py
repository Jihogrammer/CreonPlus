from typing import TYPE_CHECKING, Type
from win32com.client import Dispatch, WithEvents

from creon.config import constants
from creon.config import exceptions
from creon.utils.creon_connector import connect_creon

if TYPE_CHECKING:
    from creon.models import Module, EventHandler


def get_stock_cur_module() -> "Module":
    return Dispatch(constants.STOCK_CUR)


def bind_module_with_eventhandler(
    module: "Module", handler: Type["EventHandler"]
) -> "EventHandler":
    return WithEvents(module, handler)


def generate(creon_path: str, user_id: str, user_pw: str, cert_pw: str) -> None:
    try:
        connect_creon(creon_path, user_id, user_pw, cert_pw)
    except exceptions.AdminException as e:
        raise Exception("관리자 권한으로 실행해야 합니다.")
    except exceptions.CreonExecutionException as e:
        raise Exception("Creon Plus 프로세스가 정상적으로 실행되지 않았습니다.")
    except Exception as e:
        raise e
