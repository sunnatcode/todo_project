from rest_framework import status
from rest_framework.exceptions import APIException


class FileNotFoundException(APIException):
    status_code = status.HTTP_200_OK
    default_detail = {
        "message": 'File Not Provided',
        "status": status.HTTP_400_BAD_REQUEST
    }
    default_code = 'error'
