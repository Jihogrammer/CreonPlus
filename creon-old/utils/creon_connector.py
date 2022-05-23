def __check_admin() -> None:
    import ctypes
    from creon.config.exceptions import AdminException

    if not ctypes.windll.shell32.IsUserAnAdmin():
        raise AdminException()


def __kill_before_process() -> None:
    import os

    os.system("taskkill /IM coStarter* /F /T")
    os.system("taskkill /IM CpStart* /F /T")
    os.system("wmic process where \"name like '%coStarter%'\" call terminate")
    os.system("wmic process where \"name like '%CpStart%'\" call terminate")


def __login_creon(creon_path: str, user_id: str, user_pw: str, cert_pw: str) -> None:
    from pywinauto.application import Application

    Application().start(
        f"{creon_path} /prj:cp /id:{user_id} /pwd:{user_pw} /pwdcert:{cert_pw} /autostart"
    )


def __wait_for_connection() -> None:
    from time import sleep

    # from creon.utils.creon_manager import is_connected
    from creon.config.exceptions import CreonExecutionException

    from win32com.client import Dispatch
    from creon.config import constants

    __creon_plus_cybos = Dispatch(constants.CYBOS)

    def is_connected():
        return __creon_plus_cybos.IsConnect

    TIME_OUT = 100
    time = 0
    while not is_connected() and time < TIME_OUT:
        sleep(1)
        time += 1
    if time > TIME_OUT:
        raise CreonExecutionException()


def connect_creon(creon_path: str, user_id: str, user_pw: str, cert_pw: str) -> None:
    __check_admin()
    __kill_before_process()
    __login_creon(creon_path, user_id, user_pw, cert_pw)
    __wait_for_connection()
