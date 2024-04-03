from . import views
from django.urls import path

urlpatterns = [
    path('post/', views.create_post.as_view(), name='create-post'),
    path('post/all/', views.get_post.as_view(), name='get-post'),
    path('post/<str:pk>/', views.gup_post.as_view(), name='gup-post'),
    path('comment/', views.create_comment.as_view(), name='create-comment'),
    path('comment/all/', views.get_all_comment.as_view(), name='get-comment'),
    path('comment/<str:pk>/all/', views.get_comment.as_view(), name='get-comment'),
    path('comment/<str:pk>/', views.gup_comment.as_view(), name='gup-comment'),
    
   

]

""" path('blog/', views.create_blog.as_view(), name='create-blog'),
    path('blog/all/', views.get_all_blog.as_view(), name='all-blog'),"""