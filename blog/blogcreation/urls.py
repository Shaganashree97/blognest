from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloglist, name="blog"),
    path('base/',views.base, name="base"),
    path('bloglist/',views.bloglist,name="blog"),
    path('create_blog/',views.create_blog,name="blogcreate"),
]