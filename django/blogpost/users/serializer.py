from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from blogpost import custom_exceptions


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',"username",'email','password','first_name','last_name']

class RegisterSerializer(serializers.ModelSerializer):
    #id = serializers.CharField(source='_id', read_only = True)
    email = serializers.EmailField( required = True, validators = [UniqueValidator(queryset = CustomUser.objects.all())])
    password = serializers.CharField(required = True, write_only = True, validators = [validate_password])
    password2 = serializers.CharField(required = True, write_only = True)
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise custom_exceptions.password_mismatch()
        
        '''if  CustomUser.objects.filter(username = data['username']).exists():
            print(True)
            raise custom_exceptions.already_exists(username=data['username'])
        return data'''
    
    class Meta:
        model = CustomUser
        fields = ['_id',"username",'email','password','password2','first_name','last_name']
        extra_kwargs = { "username": {"error_messages": {"username": "Give yourself a username"}}, "first_name" : {"required": True}, "last_name" : {"required": True}}
        #extra_kwargs = {"username": {"error_messages": {"required": "Give yourself a username"}}}
    
        
    
        
    def create(self, validated_data):
        if CustomUser.objects.filter(username=validated_data['username']).exists():
            raise ({"username": "This username is already in use. Please choose a different one."})
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
    
    def validate(self, data):
        username = data.get('username','')
        password = data.get('password','')
        try:
            CustomUser.objects.get(username = username)
            user = auth.authenticate(username=username,password=password)
            if not user:
                raise custom_exceptions.Invalid_credentials()
            token = self.get_token(user)
            data = { 
                'token': str(token.access_token),
                'email': user.email,
                'username': user.username,
                'firstname': user.first_name, 
                'lastname' : user.last_name
            }
            return data
        except CustomUser.DoesNotExist:
            raise custom_exceptions.Not_Found(name="User")
        
        
        
    

    
        