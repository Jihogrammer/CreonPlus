from abc import abstractmethod
from typing import List, Union
from creon.models.modules import BaseModule


class StockChart(BaseModule):
    """주식, 업종, ELW의 차트데이터를 수신합니다.

    See Also
    --------
    - https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=102
    """

    @abstractmethod
    def SetInputValue(self, type: int, value: Union[str, int, List[int]]) -> None:
        """type에 해당하는 입력데이터를 value 값으로 지정합니다.

        Parameters
        ----------
        - `type` & `value`
            - `0`: 종목코드 - 주식(A003540), 업종(U001), ELW(J517016) 등의 종목코드
            - `1`: 요청구분 - `char` i.e. `ord('1')`
                - `'1'`: 기간
                - `'2'`: 개수
            - `2`: 요청종료일 - `int` YYYYMMDD 형식 i.e. `19940614`
            - `3`: 요청시작일 - `int` YYYYMMDD 형식 i.e. `19940614`
            - `4`: 요청개수 - `int` 요청할 데이터의 개수
            - `5`: 필드 - `List[int]` 필드 배열
                - `0`: 날짜
                - `1`: 시간(hhmm)
                - `2`: 시가
                - `3`: 고가
                - `4`: 저가
                - `5`: 종가
                - `6`: 전일대비 - 반드시 대비부호(37)와 같이 요청해야 함
                - `8`: 거래량 - 정밀도 만 원 단위
                - `9`: 거래대금
                - `10`: 누적체결매도수량 - 호가비교방식
                - `11`: 누적체결매수수량 - 호가비교방식
                - `12`: 상장주식수
                - `13`: 시가총액
                - `14`: 외국인주문한도수량
                - `15`: 외국인주문가능수량
                - `16`: 외국인현보유수량
                - `17`: 외국인현보유비율
                - `18`: 수정주가일자 - `int` YYYYMMDD
                - `19`: 수정주가비율
                - `20`: 기관순매수
                - `21`: 기관누적순매수
                - `22`: 등락주선
                - `23`: 등락비율
                - `24`: 예탁금
                - `25`: 주식회전율
                - `26`: 거래성립률
                - `37`: 대비부호 - `char`
                    - `'0'`: 판단불가/초기값/거래무
                    - `'1'`: 상한
                    - `'2'`: 상승
                    - `'3'`: 보합
                    - `'4'`: 하한
                    - `'5'`: 하락
                    - `'6'`: 기세상한
                    - `'7'`: 기세상승
                    - `'8'`: 기세하한
                    - `'9'`: 기세하락
            - `6`: 차트구분 - `char`
                - `'D'`: 일
                - `'W'`: 주
                - `'M'`: 월
                - `'m'`: 분
                - `'T'`: 틱
            - `7`: 주기 - default 1
            - `8`: 갭보정여부 - `char`
                - `'0'`: 갭무보정 (default)
                - `'1'`: 갭보정
            - `9`: 수정주가(char)
                - `'0'`: 무수정주가 (default)
                - `'1'`: 수정주가
            - `10`: 거래량구분(char)
                - `1`: 시간외거래량 모두 포함 (default)
                - `2`: 장종료시간외거래량만포함
                - `3`: 시간외거래량모두제외
                - `4`: 장전시간외거래량만포함
        """
