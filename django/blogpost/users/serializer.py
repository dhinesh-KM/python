from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import timedelta,datetime,timezone

class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',"username",'email','password','first_name','last_name']

class RegisterSerializer(serializers.ModelSerializer):
    #id = serializers.CharField(source='_id', read_only = True)
    email = serializers.EmailField( required = True, validators = [UniqueValidator(queryset = CustomUser.objects.all())])
    password = serializers.CharField(required = True, write_only = True, validators = [validate_password])
    password2 = serializers.CharField(required = True, write_only = True)
    
    
    class Meta:
        model = CustomUser
        fields = ['_id',"username",'email','password','password2','first_name','last_name']
        extra_kwargs = { "username": {"error_messages": {"username": "Give yourself a username"}}, "first_name" : {"required": True}, "last_name" : {"required": True}}
        #extra_kwargs = {"username": {"error_messages": {"required": "Give yourself a username"}}}
    
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError({"username":"Username already exists"})
        return value
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "password fields didn't match"})
        return data
        
    def create(self, validated_data):
        if CustomUser.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already in use. Please choose a different one."})
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
    

        