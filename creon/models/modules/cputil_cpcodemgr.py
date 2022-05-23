from abc import ABCMeta, abstractmethod
from typing import Any

from creon.models.enums.cpe_market_kind import CPE_MARKET_KIND


class CpCodeMgr(metaclass=ABCMeta):
    """Creon Plus 관리 모듈

    실제로는 더 많은 메서드가 존재하나,
    먼저 사용하는 메서드 위주로 정리하고 천천히 업데이트 하겠습니다.

    See Also
    --------
    - `creon.apis.code_manager`
    - http://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=287&seq=11
    """

    @abstractmethod
    def CodeToName(self, code: str) -> str:
        pass

    @abstractmethod
    def GetStockIndustryCode(self, code: str) -> Any:
        """code에 해당하는 증권전산업종코드를 반환한다.

        Returns
        -------
        증권전산업종코드: 뭐가 있는지는 확인해봐야 함
        """

    @abstractmethod
    def GetStockMarketKind(self, code: str) -> int:
        """code에 해당하는 소속부를 반환한다.

        Returns
        --------
        - 0: 구분없음
        - 1: 거래소
        - 2: 코스닥
        - 3: K-OTC
        - 4: KRX
        - 5: KONEX
        """

    @abstractmethod
    def GetStockStatusKind(self, code: str) -> int:
        """code에 해당하는 주식 상태를 반환한다.

        Returns
        -------
        - 0: 정상
        - 1: 거래정지
        - 2: 거래중단
        """

    @abstractmethod
    def GetStockGroupCode(self, code: str) -> str:
        """code에 해당하는 그룹(계열사)코드 반환한다."""

    @abstractmethod
    def GetStockSectionKind(self, code: str) -> str:
        """code에 해당하는 부구분코드를 반환한다.

        Returns
        -------
        - 0: 구분없음
        - 1: 주권
        - 2: 투자회사
        - 3: 부동산투자회사
        - 4: 선박투자회사
        - 5: 사회간접자본투융자회사
        - 6: 주식예탁증서
        - 7: 신수인수권증권
        - 8: 신주인수권증서
        - 9: 주식워런트증권
        - 10: 상장지수펀드
        - 11: 수익증권
        - 12: 해외ETF
        - 13: 외국주권
        - 14: 선물
        - 15: 옵션
        - 16: KONEX
        - 17: ETN
        """

    @abstractmethod
    def GetStockYdClosePrice(self, code: str) -> int:
        """code에 해당하는 전일종가를 반환한다."""

    @abstractmethod
    def GetStockListByMarket(self, type: int) -> list:
        """시장 구분에 따른 주식종목배열을 반환한다.

        Parameters
        ----------
        - 1: 거래소(KOSPI)
        - 2: 코스닥
        - 3: K-OTC
        - 4: KRX
        - 5: KONEX
        """
