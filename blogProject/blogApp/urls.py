from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

urlpatterns = format_suffix_patterns([
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>/',views.PostDetail.as_view(), name='post_detail'),
    path('register/',views.UserRegistration.as_view(), name='register_user' ),
])



