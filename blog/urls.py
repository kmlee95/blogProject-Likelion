from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:blog_id>',views.detail,name='detail'),
    path('edit/<int:blog_id>',views.edit, name="edit"),
    path('delete/<int:blog_id>',views.delete, name="delete"),
    path('newblog/', views.blogpost, name="newblog"),
    path('search', views.search, name="search"),
]


#name은 html에서 이름으로 사용하기위해 작성.