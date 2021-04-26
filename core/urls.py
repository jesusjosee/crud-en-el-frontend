from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-productos/', views.listar_producto, name='listar_productos'),
    path('modificar-producto/<int:id>/', views.modificar_producto, name= 'modificar_producto'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name= 'eliminar_producto'),
    path('registro/', views.registro, name='registro'),


]