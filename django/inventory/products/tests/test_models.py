from django.test import TestCase
from products.models import product
# Create your tests here.

class ProductTest(TestCase):
    
    def setUp(self):
        product.objects.create(name='cookies', price=30, quantity=10, discount = 0)
        product.objects.create(name='rice', price=50, quantity=5.000, discount = 2)
        
    def test_product_field(self):
        p1 = product.objects.get(name='cookies')
        p2 = product.objects.get(name='rice')
        self.assertEqual(p1.__str__(),'cookies have a quantity of 10.0 with a price of 30.0 with 0 percent discount' )
        self.assertEqual(p2.__str__(),'rice have a quantity of 5.0 with a price of 50.0 with 2 percent discount' )
        
    def test_name_maxlength(self):
        p = product.objects.get(name='cookies')
        m_length = p._meta.get_field("name").max_length
        self.assertEqual(m_length,50)