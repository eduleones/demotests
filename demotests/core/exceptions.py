from rest_framework.exceptions import APIException


class EmptyFileError(APIException):
    status_code = 400
    default_detail = "Empty file."
    default_code = "empty_file"
