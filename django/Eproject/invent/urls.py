from django.urls import path
from . import views
from invent.views import ProductDetailView

urlpatterns = [
   path('',views.display_all_products,name='display_all'),
   # path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
   path('report/',views.sales_report,name="report")
]