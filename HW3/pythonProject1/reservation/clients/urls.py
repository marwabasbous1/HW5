from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('add/', views.add, name='add'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('add-client/', views.add_client, name='add_client'),
    path('client-list/', views.client_list, name='client_list'),
]
