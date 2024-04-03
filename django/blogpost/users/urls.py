from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('user/', views.Post_User.as_view(),name='post_user'),
    path('user/all/', views.Get_All_User.as_view(),name='get_all_user'),
    path('user/<str:pk>/',views.gud_user.as_view(),name='get_update_delete_user'),
    path('login/',views.LoginView.as_view(),name = 'login_user'),
    #path('token/',TokenObtainPairView.as_view(),name = 'login_user'),
    path('refresh/',TokenRefreshView.as_view(),name = 'refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
