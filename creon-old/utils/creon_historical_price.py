from typing import TYPE_CHECKING, Any
from win32com.client import Dispatch

from creon.config import constants

if TYPE_CHECKING:
    from creon.modules import CP_STOCK_CHART


__creon_stock_chart: "CP_STOCK_CHART" = Dispatch(constants.STOCK_CHART)


def request_min_price_by_date(
    code: str, start_date: int, end_date: int
) -> list[list[Any]]:
    __creon_stock_chart.SetInputValue(0, code)
    __creon_stock_chart.SetInputValue(1, ord("1"))  # 기간 조회
    __creon_stock_chart.SetInputValue(2, end_date)
    __creon_stock_chart.SetInputValue(3, start_date)
    __creon_stock_chart.SetInputValue(5, [0, 2, 3, 4, 5, 8])  # 날짜,시가,고가,저가,종가,거래량
    __creon_stock_chart.SetInputValue(6, ord("D"))  # 분봉
    __creon_stock_chart.SetInputValue(9, ord("1"))  # 수정주가

    __creon_stock_chart.BlockRequest()

    payload: list[list[Any]] = []
    data_size = __creon_stock_chart.GetHeaderValue(3)

    for i in range(data_size):
        data = []
        data.append(__creon_stock_chart.GetDataValue(0, i))
        data.append(__creon_stock_chart.GetDataValue(1, i))
        data.append(__creon_stock_chart.GetDataValue(2, i))
        data.append(__creon_stock_chart.GetDataValue(3, i))
        data.append(__creon_stock_chart.GetDataValue(4, i))
        data.append(__creon_stock_chart.GetDataValue(5, i))
        payload.append(data)

    return payload
