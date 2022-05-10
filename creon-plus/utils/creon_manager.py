from win32com.client import Dispatch

import constants


__creon_plus_cybos = Dispatch(constants.CYBOS)


def is_connected():
    return __creon_plus_cybos.IsConnect
