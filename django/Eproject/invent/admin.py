from django.contrib import admin
from .models import product
#from invent.models import product
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ('product_id','name','price','quantity','discount')
    
admin.site.register(product,productAdmin) 