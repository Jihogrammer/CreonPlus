import os, ctypes
from time import sleep
from pywinauto.application import Application

from utils.creon_manager import is_connected
from models.exceptions import AdminException, CreonExecutionException

def __is_admin() -> bool:
    return ctypes.windll.shell32.IsUserAnAdmin()


def __kill_before_process() -> None:
    os.system('taskkill /IM coStarter* /F /T')
    os.system('taskkill /IM CpStart* /F /T')
    os.system('wmic process where "name like \'%coStarter%\'" call terminate')
    os.system('wmic process where "name like \'%CpStart%\'" call terminate')


def __login_creon(app: 'Application', creon_path: str, user_id: str, user_pw: str, cert_pw: str) -> None:
    app.start(f'{creon_path} /prj:cp /id:{user_id} /pwd:{user_pw} /pwdcert:{cert_pw} /autostart')


def __wait_for_connection() -> bool:
    TIME_OUT = 100
    time = 0
    while not is_connected() and time < TIME_OUT:
        sleep(1)
        time += 1
    return time < TIME_OUT


def connect_creon(creon_path: str, user_id: str, user_pw: str, cert_pw: str) -> None:
    if not __is_admin(): raise AdminException
    __kill_before_process()
    __login_creon(Application(), creon_path, user_id, user_pw, cert_pw)
    if not __wait_for_connection(): raise CreonExecutionException
