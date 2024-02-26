# forms.py
from django import forms

class ProductForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100)
    quantity = forms.IntegerField(label='Quantity', min_value=1)
