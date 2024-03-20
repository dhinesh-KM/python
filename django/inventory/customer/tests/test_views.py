import json
from rest_framework import status
from ..models import CustomUser
from ..serializer import UserSerializer
from django.test import TestCase,Client
from django.urls import reverse

client = Client()

class get_all_users(TestCase):
    
    def setUp(self):
        CustomUser.objects.create(username = "kumar", password = '0000',country = 'India', email = '123@gmail.com')
        CustomUser.objects.create(username = "vijay", password = '1111',country = 'USA', email = '456@gmail.com')
        CustomUser.objects.create(username="john", password="password123", country="Canada", email="john@example.com")
        CustomUser.objects.create(username="alice", password="secret", country="Australia", email="alice@example.com")
        CustomUser.objects.create(username="bob", password="qwerty", country="Brazil", email="bob@example.com")
        
    def test_all_users(self):
        response = self.client.get(reverse('get_post_user'))
        
        p = CustomUser.objects.all()
        serialize = UserSerializer(p,many=True)
        
        self.assertEqual(response.data, {'error': False, 'data': serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class post_user(TestCase):
    def setUp(self):
        self.valid_payload = {"username": "kumar", "password": "0000", "country": "India", "email": "123@gmail.com"}

        self.invalid_payload = {"username": "vijay","password": "1111","country": "USA","email": "456@gmail.com"}

        
    def test_post_valid_product(self):
        response = client.post(reverse("get_post_user"), data = json.dumps(self.valid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_post_invalid_product(self):
        response = client.post(reverse("get_post_user"), data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    