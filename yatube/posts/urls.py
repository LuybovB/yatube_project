from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name=''),
    path('posts/', views.group_list, name='group_name'),
    path('group/<slug:slug>/', views.group_posts),
]