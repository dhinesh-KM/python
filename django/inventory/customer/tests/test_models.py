from django.test import TestCase
from ..models import CustomUser
# Create your tests here.
class ProductTest(TestCase):
    
    def setUp(self):
        CustomUser.objects.create(username = "kumar", password = '0000',country = 'India', email = '123@gmail.com')
        CustomUser.objects.create(username = "vijay", password = '1111',country = 'USA', email = '456@gmail.com')

    def test_user_field(self):
        p1 = CustomUser.objects.get(username = "kumar")
        p2 = CustomUser.objects.get(username = "vijay")
        self.assertEqual(p1.__str__(),'kumar with a 0000 live in India' )
        self.assertEqual(p2.__str__(),'vijay with a 1111 live in US' )