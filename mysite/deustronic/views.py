from django.shortcuts import get_list_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.conf import settings

# Create your views here.
def inicio(request):
    componentes = get_list_or_404(Componente.objects.order_by('componente_nombre'));
    productos = get_list_or_404(Producto.objects.order_by('producto_nombre'));
    clientes = get_list_or_404(Cliente.objects.order_by('cliente_nombreEmpresa'));
    pedido = get_list_or_404(Pedido.objects.order_by('pedido_referencia'));
    
    context = {
        'componentes': componentes,
        'productos': productos,
        'clientes': clientes,
        'pedido': pedido,
    }
    return render(request, 'pagPrincipal.html', context)

# -- VISTAS DE AÑADIR --  # 

# AÑADIR CLIENTE #
class AnyadirClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, 'anyadir_cliente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_cliente.html', {'form': form})

# AÑADIR PRODUCTO #
class AnyadirProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        return render(request, 'anyadir_producto.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_producto.html', {'form': form})
    

# AÑADIR COMPONENTE #
class AnyadirComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadir_componente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_componente.html', {'form': form})
    
# AÑADIR PEDIDO #
class AnyadirPedidoView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        return render(request, 'anyadir_pedido.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_pedido.html', {'form': form})

# -- VISTAS DE VER --  #

# VER PEDIDO #
class VerPedidoView(View):
    def get(self, request, *args, **kwargs):
        pedido = get_list_or_404(Pedido.objects.order_by('pedido_referencia'))
        context = {
            'pedido': pedido,
        }
        return render(request, 'ver_pedido.html', context)
    
    def post(self, request, *args, **kwargs):
        pedido = get_list_or_404(Pedido.objects.order_by('pedido_referencia'))
        context = {
            'pedido': pedido,
        }
        return render(request, 'ver_pedido.html', context)

# VER COMPONENTE #
class VerComponenteView(View):
    def get(self, request, *args, **kwargs):
        Componente = get_list_or_404(Componente.objects.order_by('componente_referencia'))
        context = {
            'componente': Componente,
        }
        return render(request, 'ver_componente.html', context)
    
    def post(self, request, *args, **kwargs):
        pedido = get_list_or_404(Componente.objects.order_by('componente_referencia'))
        context = {
            'componente': Componente,
        }
        return render(request, 'ver_componente.html', context)
    
# VER CLIENTE #
class VerClienteView(View):
    def get(self, request, *args, **kwargs):
        cliente = get_list_or_404(Cliente.objects.order_by('cliente_referencia'))
        context = {
            'cliente': cliente,
        }
        return render(request, 'ver_cliente.html', context)
    
    def post(self, request, *args, **kwargs):
        cliente = get_list_or_404(Pedido.objects.order_by('cliente_referencia'))
        context = {
            'cliente': cliente,
        }
        return render(request, 'ver_cliente.html', context)

# VER PRODUCTO #
class VerProductoView(View):
    def get(self, request, *args, **kwargs):
        Producto = get_list_or_404(Producto.objects.order_by('producto_referencia'))
        context = {
            'producto': Producto,
        }
        return render(request, 'ver_producto.html', context)
    
    def post(self, request, *args, **kwargs):
        Producto = get_list_or_404(Producto.objects.order_by('producto_referencia'))
        context = {
            'producto': Producto,
        }
        return render(request, 'ver_producto.html', context)

# VER PEDIDO CLIENTE #
class VerPedidoClienteView(View):
     def get(self, request, *args, **kwargs):
            Pedido = get_list_or_404(Producto.objects.order_by('producto_referencia'))
        context = {
            'producto': Producto,
        }
        return render(request, 'detalle_cliente.pedido.html', context)
    
    def post(self, request, *args, **kwargs):
        Producto = get_list_or_404(Producto.objects.order_by('producto_referencia'))
        context = {
            'producto': Producto,
        }
        return render(request, 'detalle_cliente.pedido.html', context)

def pedidos(request):
    return render(request, 'gestionar_pedidos.html')

def catalogo(request):
    return render(request, 'ver_catalogo.html')

def contacto(request):
    return render(request, 'contact.html')

def signin(request):
    
    return render(request, 'signin.html')

def singup(request):
    context = {
        
    }
    return render(request, 'singup.html', context)
