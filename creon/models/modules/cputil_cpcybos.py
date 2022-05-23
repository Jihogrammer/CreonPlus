from abc import ABCMeta


class CpCybos(metaclass=ABCMeta):
    """Creon Plus 관리 모듈

    실제로는 더 많은 메서드가 존재하나,
    먼저 사용하는 메서드 위주로 정리하고 천천히 업데이트 하겠습니다.

    See Also
    --------
    - `creon.utils.connector`
    - https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=287&seq=2
    """

    @property
    def IsConnect() -> int:
        """Creon 연결 여부

        Returns
        -------
        - `0`: 연결끊김
        - `1`: 연결정상
        """

    @property
    def ServerType() -> int:
        """연결된 서버 종류

        Returns
        -------
        - `0`: 연결끊김
        - `1`: CybosPlus 서버
        - `2`: HTS 보통서버
        """

    @property
    def LimitRequestRemainTime() -> int:
        """요청 대기 시간 (milisecond)

        요청 개수를 재계산하기까지 남은 시간을 반환합니다.
        즉, 리턴한 시간 동안 남은 요청 개수보다 더 요청하면 요청이 제한됩니다.
        """
