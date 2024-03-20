from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    username = serializers.CharField(help_text='')
    
    
    class Meta:
        model = CustomUser
        fields = ['id',"username",'email','password','country']
        
    
        