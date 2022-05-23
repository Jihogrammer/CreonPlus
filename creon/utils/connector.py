"""Creon Plus Connector

전역에 모듈을 할당하면 이후 로그인 과정에서
모듈 통제권을 잃고 프로세스가 종료되는 현상이 있다.
따라서 is_connected 메서드에서 모듈을 매번 호출하는 방향으로 구성했다.

See Also
--------
- https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=287&seq=2
"""


def is_connected() -> bool:
    """Creon Module에서 연결 여부를 확인

    연결 상태를 확인하는 모듈의 경우 싱글톤으로 관리하는 것은 불안정하다.
    dll을 불러오는 환경에서 `Dispatch` 비용은 크지 않으므로,
    상태를 점검하는 경우에는 항상 모듈을 갱신해서 확인하는 편이 안전하다.
    """
    from creon.utils.dispatcher import get_cp_cybos_module

    return get_cp_cybos_module().IsConnect == 1


def connect(
    user_id: str,
    user_pw: str,
    cert_pw: str,
    creon_path: str = "C:\\CREON\\STARTER\\coStarter.exe",
) -> None:
    """Creon Plus 연결"""
    __check_admin()
    __kill_before_process()
    __login_creon(user_id, user_pw, cert_pw, creon_path)
    __wait_for_connection()


def __check_admin() -> None:
    """관리자 권한으로 실행했는지 확인"""
    import ctypes
    from creon.config.exceptions import AdminException

    if not ctypes.windll.shell32.IsUserAnAdmin():
        raise AdminException()


def __kill_before_process() -> None:
    """이전에 실행 중이던 Creon Plus 종료

    예전에는 `coStarter`라는 친구를 종료해줘야 했는데,
    최근에는 `DibServer`를 종료해주어야 재실행에 문제가 없다.
        - `os.system("taskkill /IM coStarter* /F /T")`
        - `os.system("wmic process where \"name like '%coStarter%'\" call terminate")`

    또한 `CpStart` 없이 `DibServer`만 실행되어도 제대로 동작한다.
    추측이지만 `CpStart`는 최초 로그인에만 관여하고,
    연결을 맺은 후에는 `DibServer`가 주관한다.
    이는 조회 시에만 정상적으로 동작하는 것을 확인했고,
    실제 주문 등 복잡한 요구사항에도 반응하는지는 확인을 해야 한다.
    그러나 전체적으로 Creon을 사용하는 데 지장이 없으므로
    웬만하면 그대로 두는 것으로 하자.
    """
    import os

    os.system("taskkill /IM CpStart* /F /T")
    os.system("taskkill /IM DibServer* /F /T")
    os.system("wmic process where \"name like '%CpStart%'\" call terminate")
    os.system("wmic process where \"name like '%DibServer%'\" call terminate")


def __login_creon(user_id: str, user_pw: str, cert_pw: str, creon_path: str) -> None:
    """Creon Plus을 실행하고 로그인 시도"""
    from pywinauto.application import Application

    Application().start(
        f"{creon_path} /prj:cp /id:{user_id} /pwd:{user_pw} /pwdcert:{cert_pw} /autostart"
    )


def __wait_for_connection(timed_out: int = 100) -> None:
    """Creon Plus가 실행되기까지 기다림

    Creon Plus는 완전히 실행되기까지 시간이 꽤 걸린다.
    업데이트 등으로 인해 100초 정도의 간격을 주는 것이 합당하다고 판단했다.

    Warning
    -------
    또한 예외적으로 팝업창이 뜨는 경우가 발생하는데,
    이 때 팝업창을 닫지 않을 경우 timed out이 발생하여 예외가 발생한다.
    기술적으로 처리하는 것보다 직접 닫아주는 것으로 처리하도록 한다.

    비슷하게 selenium 등에서는 웹브라우저 환경이라 경고창을 처리할 수 있으나,
    크레온은 클라이언트 환경이라 방법을 찾기 어려운 상황이다.
    """
    from time import sleep
    from creon.config.exceptions import CreonExecutionException

    spent_time = 0
    while not is_connected():
        sleep(1)
        spent_time += 1
        if spent_time > timed_out:
            raise CreonExecutionException()
