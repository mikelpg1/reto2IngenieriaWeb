"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='base'),
    path('anyadirPedidoProducto', views.anyadirPedidoView.as_view, name='anyadirPedidoProducto'),
    path('anyadirComponenteProducto', views.anyadirComponenteProductoView.as_view, name='anyadirComponenteProducto'),
    path('anyadirProducto', views.anyadirProductoView.as_view, name='anyadirProducto'),
    path('anyadirPedido', views.anyadirPedidoView.as_view, name='anyadirPedido'),
    path('anyadirComponente', views.anyadirComponenteView.as_view, name='anyadirComponente'),
    path('anyadirCliente', views.anyadirClienteView.as_view, name='anyadirCliente'),
    path('detalleProducto/<int:pk>/', views.detalleProductoView.as_view(), name='detalleProducto'),
    path('detalleCliente/<int:pk>/', views.detalleClienteView.as_view(), name='detalleCliente'),
    path('detalleProducto/<int:pk>/', views.detalleComponenteView.as_view(), name='detalleComponente'),
    path('detalleProducto/<int:pk>/', views.detallePedidoView.as_view(), name='detallePedido'),
    path('eliminarPedido/<int:pk>/', views.eliminarPedidoView.as_view(), name='eliminarPedido'),
    path('eliminarComponente/<int:pk>/', views.eliminarComponenteView.as_view(), name='eliminarComponente'),
    path('eliminarProducto/<int:pk>/', views.eliminarProductoView.as_view(), name='eliminarProducto'),
    path('eliminarCliente/<int:pk>/', views.eliminarClienteView.as_view(), name='eliminarCliente'),
    
]
