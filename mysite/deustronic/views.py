from multiprocessing import context
from pyexpat import model
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic.edit import DeleteView, UpdateView
from django.http import HttpResponse


# Create your views here.
def listadoCliente(request):
    cliente = get_list_or_404(Cliente);
    
    context = {
        'clientes': cliente,
    }
    return render(request, "listadoCliente.html", context)

# -- VISTAS DE Listado --  # 

def inicio(request):
    producto = get_list_or_404(Producto);
    cliente = get_list_or_404(Cliente);
    componente = get_list_or_404(Componente);
    pedido = get_list_or_404(Pedido)


    context = {
        'productos': producto,
        'clientes': cliente,
        'pedidos': pedido,
        'componentes': componente
    }
    return render(request, "pagPrincipal.html", context)

def listadoProducto(request):
    producto = get_list_or_404(Producto)
    context = {
        'productos': producto,
    }
    return render(request, "listadoProducto.html", context)

def listadoPedido(request):
    pedido = get_list_or_404(Pedido)
    producto = get_list_or_404(Producto)

    context = {
        'pedidos': pedido,
        'productos': producto
    }
    return render(request, "listadoPedido.html", context)



def listadoComponente(request):
    componente = get_list_or_404(Componente)
    context = {
        'componentes': componente,
    }
    return render(request, "listadoComponente.html", context)

# -- VISTAS DE AÑADIR --  # 


# AÑADIR CLIENTE #
class anyadirClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, 'anyadirCliente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirCliente.html', {'form': form})

class anyadirProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        return render(request, 'anyadirProducto.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirProducto.html', {'form': form})
    
class anyadirComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadirComponente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirComponente.html', {'form': form})
    
class anyadirPedidoView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        return render(request, 'anyadirPedido.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirPedido.html', {'form': form})

class anyadirComponenteProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadirComponenteProducto.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirComponenteProducto.html', {'form': form})
    
# -- VISTAS DE VER --  #

# VER PEDIDO #
def detallePedidoView(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    
    context = {
        'pedido': pedido,
    }
    return render(request, 'detallePedido.html', context)

def detalleComponenteView(request, pk):
    componente = get_object_or_404(Componente, pk=pk)
    return render(request, 'detalleComponente.html', {'componente': componente})
    
def detalleClienteView(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = Pedido.objects.filter(cliente=cliente)
    
    context = {
        'cliente': cliente,
        'pedidos': pedidos
    }
    return render(request, 'detalleCliente.html', context)

def detalleProductoView(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    componentes = get_list_or_404(Componente.objects.order_by('nombre'))
    
    context = {
        'producto': producto,
        'componentes': componentes
    }
    return render(request, 'detalleProducto.html', context)

class eliminarProductoView(DeleteView):
    model = Producto  
    template_name = 'eliminarProducto.html'  
    success_url = reverse_lazy('base') 
    
class eliminarComponenteView(DeleteView):
    model = Componente  
    template_name = 'eliminarComponente.html'  
    success_url = reverse_lazy('base')
    
class eliminarClienteView(DeleteView):
    model = Cliente  
    template_name = 'eliminarCliente.html'  
    success_url = reverse_lazy('base')
    
class eliminarPedidoView(DeleteView):
    model = Pedido
    template_name = 'eliminarPedido.html'
    success_url = reverse_lazy('base')
    
class modificarProductoView(UpdateView):
    model = Producto
    template_name = 'modificarProducto.html'
    fields = ['nombre', 'categoria', 'descripcion', 'precio']
    success_url = reverse_lazy('base')

class modificarComponenteView(UpdateView):
    model = Componente
    template_name = 'modificarComponente.html'
    fields = ['nombre', 'marca']
    success_url = reverse_lazy('base')
        
        
class modificarClienteView(UpdateView):
    model = Cliente
    template_name = 'modificarCliente.html'
    fields = ['CIF', 'nombreEmpresa', 'direccion', 'datosContacto']
    success_url = reverse_lazy('base')
        
class modificarPedidoView(UpdateView):
    model = Pedido
    template_name = 'modificarPedido.html'
    fields = ['cantidadproducto', 'precioTotal']
    success_url = reverse_lazy('base')

