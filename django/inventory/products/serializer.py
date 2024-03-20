from rest_framework import serializers
from .models import product
from customer.models import CustomUser

class ProductSerializer(serializers.ModelSerializer): 
    id = serializers.CharField(source='_id', read_only = True)
    #user = serializers.ReadOnlyField(source = 'user.id')
    class Meta:
        model = product
        fields = "__all__"


        
'''class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user'''