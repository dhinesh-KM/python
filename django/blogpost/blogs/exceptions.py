from rest_framework.exceptions import APIException
from rest_framework import status

class Not_Found(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    error = True
    #msg = 'Post not found.'

    def __init__(self, detail=None,name=None):
        if detail is None:
            detail = {'error': self.error, 'msg':f'{name} not found' }
        super().__init__(detail=detail, code=self.status_code)
        
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
    
