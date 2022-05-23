from email import message


class CreonIsNotGeneratedException(Exception):
    message = "Creon 연결 상태를 확인해주세요."


class AdminException(Exception):
    message = "관리자 권한으로 실행되어야 합니다."


class CreonExecutionException(Exception):
    message = "Creon Plus 실행에 문제가 발생했습니다."
