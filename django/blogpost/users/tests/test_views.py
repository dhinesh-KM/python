import json
from rest_framework import status
from ..models import CustomUser
from ..serializer import RegisterSerializer
from django.test import TestCase,Client
from django.urls import reverse
from bson import ObjectId
from rest_framework.test import APIClient

client = Client()

        
class get_all_users(TestCase):
    
    def setUp(self):
        admin_user = CustomUser.objects.create(username='admin', is_staff=True, is_superuser=True)
        admin_user.set_password('adminpass')
        admin_user.save()
        
        self.admin = admin_user
        self.client.force_login(user=admin_user)
        
        CustomUser.objects.create(username = "vimal10", password = '0000',first_name = "vimal", last_name = "nagul", email = '123@gmail.com')
        CustomUser.objects.create(username = "arun10", password = '1111',first_name = "arun", last_name = "ganesh", email = '456@gmail.com')
        #CustomUser.objects.create(username="john_doe",password="password123",first_name="John",last_name="Doe",email="john.doe@example.com")
        #CustomUser.objects.create(username="jane_smith",password="password456",first_name="Jane",last_name="Smith",email="jane.smith@example.com")
    
        
    def test_all_users(self):
        response = self.client.get(reverse('get_all_user'))
        
        p = CustomUser.objects.all()
        serialize = RegisterSerializer(p,many=True)
        print(response.data)
        self.assertEqual(response.data, {'error': False, 'data': serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class post_user(TestCase):
    def setUp(self):
        self.valid_payload = {'username': 'vimal10','password': '000000!@','password2': '000000!@','first_name': 'Vimal','last_name': 'Nagul','email': '123@gmail.com'}

        self.invalid_payload = {'username': 'vimal10','password': '000000!@','password2': '','first_name': 'Vimal','last_name': 'Nagul','email': '123@gmail.com'}

        
    def test_valid_post(self):
        response = client.post(reverse("post_user"), data=json.dumps(self.valid_payload), content_type="application/json")
        print(response.content)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_invalid_post(self):
        response = client.post(reverse("post_user"), data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


class get_user(TestCase):
    def setUp(self):
        self.john = CustomUser.objects.create(username="john_doe",password="password123",first_name="John",last_name="Doe",email="john.doe@example.com")
        self.jane =  CustomUser.objects.create(username="jane_smith",password="password456",first_name="Jane",last_name="Smith",email="jane.smith@example.com")

        
    def test_valid_user(self):
        print("*",self.john.pk)
        response = client.get(reverse('get_update_delete_user', kwargs={'pk': self.john.pk}))
        
        p = CustomUser.objects.get(pk = ObjectId(self.john.pk))
        serialize = RegisterSerializer(p)
        
        self.assertEqual(response.data, {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_invalid_user(self):
        response = client.get(reverse("get_update_delete_user", kwargs=  {'pk': '65f7c91a640f8785302bd21f'}))
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('login_user')
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com', password='testpassword', first_name='Test', last_name='User')

    def test_login(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('pk' in response.data)
        self.assertTrue('email' in response.data)
        self.assertTrue('username' in response.data)
        self.assertTrue('firstname' in response.data)
        self.assertTrue('lastname' in response.data)
    