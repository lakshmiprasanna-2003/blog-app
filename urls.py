from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/create/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/update/', views.update_blog, name='update_blog'),
    path('blog/<int:pk>/delete/', views.delete_blog, name='delete_blog'),
]
