from rest_framework.exceptions import APIException


class GetPokemonNotFoundError(APIException):
    status_code = 404
    default_detail = "pokemon not found"
    default_code = "not_found"


class GetPokemonGenericError(APIException):
    status_code = 500
    default_detail = "pokemon generic"
    default_code = "generic"
