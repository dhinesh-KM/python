#from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from customer.models import Order
from django.views.generic.detail import DetailView
from django.db.models import Sum
from django.core.serializers import serialize
from django.db.models import Q
from django.db.models import F, ExpressionWrapper, FloatField, Sum
from djongo import models
#from datetime import time,datetime,date
import datetime
#from .utils import LazyEncoder

# Create your views here.

class ProductDetailView(DetailView):
    model = product

    def render_to_response(self, context, **response_kwargs):
        # Serialize the object to JSON
        data = {
            'name': self.object.name,
            'price': str(self.object.price),  # Convert DecimalField to string
            'quantity': str(self.object.quantity),  # Convert DecimalField to string
            'discount': self.object.discount,
        }
        return JsonResponse(data)



def display_all_products(request):
    #data = serialize("json",product.objects.all())
    products = product.objects.all()
    data = [{"id":x.product_id,"name":x.name,"price":str(x.price),"quantity":str(x.name),"discount":str(x.discount)} for x in products]
    return JsonResponse(data, safe=False)

def sales_report(request):
    year =2024
    m = Order.objects.filter(o_datetime__year=year).values("prod","o_quantity").annotate(t_quan=Sum('o_quantity'))
    p = product.objects.all().values("product_id","price")
    result = [d1.get('t_quan')*d2.get('price') for d1 in m for d2 in p if d1.get('prod') == d2.get('product_id')]
    s =sum(result)
    
    
    return JsonResponse({"status":200,f"Total sales amount on {year}":s}, safe=False)