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
