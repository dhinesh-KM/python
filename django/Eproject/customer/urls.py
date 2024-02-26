from django.urls import path
from . import views
from invent.views import ProductDetailView




urlpatterns = [
    path('',views.index,name="index"),
    path('all/',views.display_all_products,name='display_all'),
    #path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('display/',views.display,name="display"),
    path('order/',views.place_order,name="order"),
    
]
 