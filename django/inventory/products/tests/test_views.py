import json
from rest_framework import status
from ..models import product
from ..serializer import ProductSerializer
from django.test import TestCase,Client
from django.urls import reverse
from bson.objectid import ObjectId

client = Client()

class get_all_products(TestCase):
    
    def setUp(self):
        product.objects.create(name="cookies", price=30, quantity=10, discount = 0)
        product.objects.create(name="rice", price=50, quantity=5.000, discount = 2)
        product.objects.create(name="Chocolate", price=25, quantity=5, discount=5)
        product.objects.create(name="Milk", price=30, quantity=100, discount=0)
        
    def test_all_products(self):
        response = client.get(reverse("get_post_product"))
        
        p = product.objects.all()
        serialize = ProductSerializer(p,many=True)
        self.assertEqual( response.data,  {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class get_product(TestCase):
    def setUp(self):
        self.cookies = product.objects.create(name="cookies", price=30, quantity=10, discount = 0)
        self.rice = product.objects.create(name="rice", price=50, quantity=5.000, discount = 2)
        
    def test_valid_product(self):
        response = client.get(reverse('get_update_delete_product', kwargs={'pk': self.cookies.pk}))
        
        p = product.objects.get(pk = ObjectId(self.cookies.pk))
        serialize = ProductSerializer(p)
        
        self.assertEqual(response.data, {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_invalid_product(self):
        response = client.get(reverse("get_update_delete_product", kwargs=  {'pk': '65f7c91a640f8785302bd21f'}))
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

        
class post_product(TestCase):
    def setUp(self):
        self.valid_payload = {"name" : "cookies", "price" : 30.0, "quantity" : 10.0, "discount" : 0}
        self.invalid_payload = {"name" : "", "price" : 30.0, "quantity" : 10.0, "discount" : 0}
        
    def test_post_valid_product(self):
        response = client.post(reverse("get_post_product"), data = json.dumps(self.valid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_post_invalid_product(self):
        response = client.post(reverse("get_post_product"), data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
class put_product(TestCase):
    def setUp(self):
        self.cookies = product.objects.create(name="cookies", price=30, quantity=10, discount = 0)
        self.rice = product.objects.create(name="rice", price=50, quantity=5.000, discount = 2)
        self.valid_payload = {"name" : "cookies", "price" : 30.0, "quantity" : 10.0, "discount" : 0}
        self.invalid_payload = {"name" : "", "price" : 30.0, "quantity" : 10.0, "discount" : 0}
        
    def test_put_valid_product(self):
        response = client.put(reverse('get_update_delete_product', kwargs={'pk': self.cookies.pk}),
                              data = json.dumps(self.valid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_put_invalid_product(self):
        response = client.put(reverse('get_update_delete_product', kwargs={'pk': self.cookies.pk}),
                              data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
class delete_product(TestCase):
    def setUp(self):
        self.cookies = product.objects.create(name="cookies", price=30, quantity=10, discount = 0)
        self.rice = product.objects.create(name="rice", price=50, quantity=5.000, discount = 2)
        
    def test_delete_valid_product(self):
        response = client.delete(reverse('get_update_delete_product', kwargs={'pk': self.cookies.pk}))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(product.objects.count(), 1)
        
    def test_delete_invalid_product(self):
        response = client.delete(reverse('get_update_delete_product', kwargs={'pk': '65f7c91a640f8785302bd21f'}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        

        
        
        
        