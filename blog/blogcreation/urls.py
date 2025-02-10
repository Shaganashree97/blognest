from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloglist, name="blog"),
    path('base/',views.base, name="base"),
    path('bloglist/',views.bloglist,name="blog"),
    path('create_blog/',views.create_blog,name="blogcreate"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]