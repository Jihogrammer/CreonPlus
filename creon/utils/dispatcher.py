from typing import TYPE_CHECKING
from win32com.client import Dispatch

from creon.config import constants

if TYPE_CHECKING:
    from creon.models.modules import CpCybos, CpCodeMgr, BaseModule


def get_cp_cybos_module() -> "CpCybos":
    return Dispatch(constants.CP_CYBOS)


def get_cp_code_mgr_module() -> "CpCodeMgr":
    return Dispatch(constants.CODE_MANAGER)


def get_stock_chart_module() -> "CpCodeMgr":
    return Dispatch(constants.CODE_MANAGER)


def get_stock_cur_module() -> "BaseModule":
    return Dispatch(constants.STOCK_CUR)
