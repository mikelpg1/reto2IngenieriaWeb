from django.urls import path
from . import views
from deustronic.views import *

urlpatterns = [
    path('inicio', inicio, name='base'),

    #path('iniciarSesion', views.iniciarSesion, name = 'iniciarSesion'),
    
    path('anyadirPedidoProducto', AnyadirPedidoView.as_view(), name='anyadirPedidoProducto'),
    path('anyadirComponenteProducto', AnyadirComponenteProductoView.as_view(), name='anyadirComponenteProducto'),
    path('anyadirProducto', AnyadirProductoView.as_view(), name='anyadirProducto'),
    path('anyadirPedido', AnyadirPedidoView.as_view(), name='anyadirPedido'),
    path('anyadirComponente', AnyadirComponenteView.as_view(), name='anyadirComponente'),
    path('anyadirCliente', AnyadirClienteView.as_view(), name='anyadirCliente'),

    
    path('detalleProducto/<int:pk>/', detalleProductoView, name='detalleProducto'),
    path('detallePedido/<int:pk>/', detallePedidoView, name='detallePedido'),
    path('detalleCliente/<int:pk>/', detalleClienteView, name='detalleCliente'),
    path('detalleComponente/<int:pk>/', detalleComponenteView, name='detalleComponente'),
    
    path('modificarProducto/<int:pk>/', ModificarProductoView.as_view(), name='modificarProducto'),
    path('modificarPedido/<int:pk>/', ModificarPedidoView.as_view(), name='modificarPedido'),
    path('modificarComponente/<int:pk>/', ModificarComponenteView.as_view(), name='modificarComponente'),
    path('modificarCliente/<int:pk>/', ModificarClienteView.as_view(), name='modificarCliente'),
    
    path('eliminarProducto/<int:pk>/', EliminarProductoView.as_view(), name='eliminarProducto'),
    path('eliminarPedido/<int:pk>/', EliminarPedidoView.as_view(), name='eliminarPedido'),
    path('eliminarComponente/<int:pk>/', EliminarComponenteView.as_view(), name='eliminarComponente'),
    path('eliminarCliente/<int:pk>/', EliminarClienteView.as_view(), name='eliminarCliente'),
    
    path('listadoProducto', views.listadoProducto, name='listadoProducto'),
    path('listadoComponente', views.listadoComponente, name='listadoComponente'),
    path('listadoPedido', views.listadoPedido, name='listadoPedido'),
    path('listadoCliente', views.listadoCliente, name='listadoCliente'),

    path('envioEmail',views.enviarCorreo, name='envioEmail'),



    

]
