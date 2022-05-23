from typing import Any
from creon.models.enums.cpe_market_kind import CPE_MARKET_KIND
from creon.utils.dispatcher import get_cp_code_mgr_module


def get_name_by_code(code: str) -> str:
    return get_cp_code_mgr_module().CodeToName(code)


def get_yesterday_close_price_by_code(code: str) -> int:
    return get_cp_code_mgr_module().GetStockYdClosePrice(code)


def get_code_list_by_market_kind(kind: CPE_MARKET_KIND) -> list[str]:
    return get_cp_code_mgr_module().GetStockListByMarket(kind.value)


def get_code_list_of_KOSPI() -> list[str]:
    return get_code_list_by_market_kind(CPE_MARKET_KIND.KOSPI)


def get_code_list_of_KOSDAQ() -> list[str]:
    return get_code_list_by_market_kind(CPE_MARKET_KIND.KOSDAQ)


def get_industry_code_by_code(code: str) -> Any:
    return get_cp_code_mgr_module().GetStockIndustryCode(code)


def get_market_by_code(code: str) -> int:
    return get_cp_code_mgr_module().GetStockMarketKind(code)


def get_status_by_code(code: str) -> int:
    return get_cp_code_mgr_module().GetStockStatusKind(code)


def get_group_code_by_code(code: str) -> str:
    return get_cp_code_mgr_module().GetStockGroupCode(code)


def get_section_by_code(code: str) -> str:
    return get_cp_code_mgr_module().GetStockSectionKind(code)
