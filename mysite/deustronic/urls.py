from django.urls import path
from . import views
from deustronic.views import *

urlpatterns = [
    path('inicio', views.inicio, name='base'),
    #path('iniciarSesion', views.iniciarSesion, name = 'iniciarSesion'),
    
    path('anyadirPedidoProducto', anyadirPedidoView.as_view(), name='anyadirPedidoProducto'),
    path('anyadirComponenteProducto', anyadirComponenteProductoView.as_view(), name='anyadirComponenteProducto'),
    path('anyadirProducto', anyadirProductoView.as_view(), name='anyadirProducto'),
    path('anyadirPedido', anyadirPedidoView.as_view(), name='anyadirPedido'),
    path('anyadirComponente', anyadirComponenteView.as_view(), name='anyadirComponente'),
    path('anyadirCliente', anyadirClienteView.as_view(), name='anyadirCliente'),

    
    path('detalleProducto/<int:pk>/', detalleProductoView, name='detalleProducto'),
    path('detallePedido/<int:pk>/', detallePedidoView, name='detallePedido'),
    path('detalleCliente/<int:pk>/', detalleClienteView, name='detalleCliente'),
    path('detalleComponente/<int:pk>/', detalleComponenteView, name='detalleComponente'),
    
    path('modificarProducto/<int:pk>/', modificarProductoView.as_view(), name='modificarProducto'),
    path('modificarPedido/<int:pk>/', modificarPedidoView.as_view(), name='modificarPedido'),
    path('modificarComponente/<int:pk>/', modificarComponenteView.as_view(), name='modificarComponente'),
    path('modificarCliente/<int:pk>/', modificarClienteView.as_view(), name='modificarCliente'),
    
    path('eliminarProducto/<int:pk>/', eliminarProductoView.as_view(), name='eliminarProducto'),
    path('eliminarPedido/<int:pk>/', eliminarPedidoView.as_view(), name='eliminarPedido'),
    path('eliminarComponente/<int:pk>/', eliminarComponenteView.as_view(), name='eliminarComponente'),
    path('eliminarCliente/<int:pk>/', eliminarClienteView.as_view(), name='eliminarCliente'),
    
    path('listadoProducto', views.listadoProducto, name='listadoProducto'),
    path('listadoComponente', views.listadoComponente, name='listadoComponente'),
    path('listadoPedido', views.listadoPedido, name='listadoPedido'),
    path('listadoCliente', views.listadoCliente, name='listadoCliente'),


]
