from enum import Enum


class CPE_MARKET_KIND(Enum):
    """시장 구분"""

    NULL = 0
    """구분없음"""
    KOSPI = 1
    """거래소"""
    KOSDAQ = 2
    """코스닥"""
    FREEBOARD = 3
    """K-OTC"""
    KRX = 4
    """KRX"""
    KONEX = 5
    """KONEX"""
