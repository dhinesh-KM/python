from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework.authtoken.views import ObtainAuthToken




urlpatterns = [
    path('products/<str:pk>/',views.gud_product.as_view(),name='get_update_delete_product'),
    path('products/', views.gp_product.as_view(),name='get_post_product'),
    #path('login/',views.Customlogin.as_view(),name = 'login_user'),
    #path('api/v1/products/<str:pk>/',views.get_update_delete_product,name='get_update_delete_product'),
    #path('api/v1/products/', views.get_post_product,name='get_post_product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)