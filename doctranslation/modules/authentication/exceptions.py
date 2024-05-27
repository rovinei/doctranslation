from rest_framework import exceptions, status
from rest_framework.serializers import ValidationError


class APIBaseException(exceptions.APIException):
    error_type = None
    title = None
    error_code = None
    detail = None

    def __init__(self, errors=None):
        super().__init__(detail=self.to_dict(errors))

    @classmethod
    def to_dict(cls, errors=None):
        return {
            'type': cls.error_type,
            'title': cls.title,
            'status': cls.status_code,
            'error_code': cls.error_code,
            'detail': cls.detail,
            'invalid_params': [
                {
                    'name': name,
                    'reason': '\n'.join(messages),
                } for name, messages in errors.items()
            ] if errors else [],
        }


class APIBaseValidationError(ValidationError):
    detail = None

    def __init__(self, fields: list):
        super().__init__(detail={f: self.detail for f in fields})


class AuthFailedException(APIBaseException):
    error_type = ''
    title = 'AuthFailed'
    detail = 'Auth Failed'
    status_code = status.HTTP_401_UNAUTHORIZED
    error_code = 1001


class OperationNotAllowedException(APIBaseException):
    error_type = ''
    title = 'OperationNotAllowed'
    detail = 'Operation Not Allowed'
    status_code = status.HTTP_403_FORBIDDEN
    error_code = 1002


class WrongParameterException(APIBaseException):
    error_type = ''
    title = 'WrongParameter'
    detail = 'Wrong Parameter'
    status_code = status.HTTP_400_BAD_REQUEST
    error_code = 1003


class NotFoundException(APIBaseException):
    error_type = ''
    title = 'NotFound'
    detail = 'Not Found'
    status_code = status.HTTP_404_NOT_FOUND
    error_code = 1004


class ServerErrorException(APIBaseException):
    error_type = ''
    title = 'ServerError'
    detail = 'Server Error'
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_code = 1005


class MethodNotAllowedException(APIBaseException):
    error_type = ''
    title = 'MethodNotAllowed'
    detail = 'Method Not Allowed'
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    error_code = 1006


class APIInvalidError(APIBaseValidationError):
    detail = 'This condition is invalid.'
