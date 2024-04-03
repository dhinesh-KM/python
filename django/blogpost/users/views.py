from rest_framework import generics,permissions
from .serializer import RegisterSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from bson.objectid import ObjectId
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate
from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from bson.errors import InvalidId
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.authentication import JWTAuthentication,JWTTokenUserAuthentication

class Post_User(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response = {'error': False,'msg': 'User created successfully','data': response.data}
        return Response(response, status=status.HTTP_201_CREATED)
    
class Get_All_User(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response = {'error': False, 'data': response.data}
        return Response(response, status= status.HTTP_200_OK)
    
class gud_user(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'pk'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

    
    
    def get_object(self):
        try:
            queryset = self.get_queryset()
            obj = queryset.get(pk=ObjectId(self.kwargs['pk']))
            self.check_object_permissions(self.request, obj)
            return obj
        
        except ObjectDoesNotExist:
            raise APIException({'error': True, 'msg': 'Post  not found ' })
        
        except InvalidId:
            raise APIException({'error': True, 'msg': f'Invalid comment Id {self.kwargs['pk']} ' })
        
        

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data})
    
    def patch(self, request, *args, **kwargs):
        response =  super().patch(request, *args, **kwargs)
        return Response({'error': False, 'data': response.data})
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'error': False, 'msg': f'User  deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
'''class LoginView(APIView):
    
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password = password)
        print('user',user,username,password)
        refresh = RefreshToken.for_user(user)
        print('r:',refresh,'a',refresh.access_token)
        return Response({'data': { 'refresh' : str(refresh), 'access': str(refresh.access_token)}})'''
    
class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get(username = request.data['username'])
        token = serializer.get_token(user)
        data = { 'token': str(token.access_token), 'refresh token': str(serializer.validated_data['refresh']) , 'email': user.email, 'username': user.username, 'firstname': user.first_name, 'lastname' : user.last_name}
        return Response({ 'error':False, 'data': data })