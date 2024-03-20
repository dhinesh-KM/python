from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('users/<int:pk>/',views.gud_user.as_view(),name='get_update_delete_user'),
    path('users/', views.gp_user.as_view(),name='get_post_user'),
    #path('login/',views.Customlogin.as_view(),name = 'login_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)