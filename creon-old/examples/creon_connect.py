from creon.utils.creon_api import generate
from creon.utils.creon_manager import is_connected


def example():
    creon_path = "C:\\CREON\\STARTER\\coStarter.exe"
    user_id = input("ID : ")
    user_pw = input("Password : ")
    cert_pw = input("Cert Password : ")

    generate(creon_path, user_id, user_pw, cert_pw)

    if is_connected():
        print("로그인 성공")
