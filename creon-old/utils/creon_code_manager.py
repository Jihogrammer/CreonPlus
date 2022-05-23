from typing import TYPE_CHECKING
from win32com.client import Dispatch

from creon.config import constants

if TYPE_CHECKING:
    from creon.modules import CP_CODE_MANAGER


__creon_code_manager: "CP_CODE_MANAGER" = Dispatch(constants.CODE_MANAGER)


def get_code_list_of_KOSPI() -> list[str]:
    return __creon_code_manager.GetStockListByMarket(1)


def get_code_list_of_KOSDAQ() -> list[str]:
    return __creon_code_manager.GetStockListByMarket(2)
