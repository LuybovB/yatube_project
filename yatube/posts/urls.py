from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('community_page', views.group_list),
]
