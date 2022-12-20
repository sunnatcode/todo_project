from rest_framework import status
from rest_framework.exceptions import APIException


class PasswordDidNotMatchException(APIException):
    status_code = 451
    default_detail = {
        "message": 'Password Did not match Exception',
        "status": 451
    }
    default_code = 'error'


class UsernameTakenException(APIException):
    status_code = 455
    default_detail = {
        "message": 'Username already taken exception',
        "status": 455
    }
    default_code = 'error'


class AlreadyTakenException(APIException):
    status_code = 455
    default_code = 'error'

    def __init__(self, key, status_code, detail=None, code=None):
        detail = {
            "message": f'{key} already exists'
        }
        AlreadyTakenException.status_code = status_code
        super().__init__(detail, code)
