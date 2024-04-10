from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import APIException


class Not_Found(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    error = True

    def __init__(self,name):
        detail = {'error': self.error, 'msg':f'{name} not found' }
        super().__init__(detail=detail, code=self.status_code)

class password_mismatch(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    error = True

    def __init__(self):
        detail = {'error': self.error, 'msg': "password fields didn't match" }
        super().__init__(detail=detail, code=self.status_code)
        
class Invalid_credentials(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    error = True

    def __init__(self):
        detail = {'error': self.error, 'msg': "Invalid credentials please try again" }
        super().__init__(detail, code=self.status_code)

        
class Invalid_Id(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    error = True
    msg = 'Invalid id'

    def __init__(self, pk=None):
        if pk is None:
            msg = self.msg
        else:
            msg = f'Ivalid pk {pk}'
            super().__init__(detail={'error': self.error, 'msg': msg}, code=self.status_code)
            
class already_exists(APIException):
    status_code = status.HTTP_409_CONFLICT
    error = True
    
    def __init__(self,username):
        detail = {'error': self.error, 'msg': f' username {username} already exists'}
        super().__init__(detail, code=self.status_code)
            
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['error'] = True
        response.data['msg'] = response.data.pop('detail', None )
        response.status_code = status.HTTP_401_UNAUTHORIZED

    return response
