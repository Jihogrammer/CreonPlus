from os import getenv
from dotenv import load_dotenv
from creon.utils.connector import connect, is_connected


load_dotenv(verbose=False)

creon_path = getenv("CREON_PATH")
user_id = getenv("CREON_USER_ID")
user_pw = getenv("CREON_USER_PW")
cert_pw = getenv("CREON_CERT_PW")

connect(user_id, user_pw, cert_pw, creon_path)
print(is_connected())
