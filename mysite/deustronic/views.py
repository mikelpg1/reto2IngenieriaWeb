from sre_constants import SUCCESS
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.
def inicio(request):
    componente = get_list_or_404(Componente);
    producto = get_list_or_404(Producto);
    cliente = get_list_or_404(Cliente);
    pedido = get_list_or_404(Pedido);
    
    context = {
        'componentes': componente,
        'productos': producto,
        'clientes': cliente,
        'pedidos': pedido
    }
    return render(request, "pagPrincipal.html", context)

# -- VISTAS DE AÑADIR --  # 

# AÑADIR CLIENTE #
class anyadirClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, 'anyadir_cliente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_cliente.html', {'form': form})

class anyadirProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        return render(request, 'anyadir_producto.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadir_producto.html', {'form': form})
    
class anyadirComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadir_componente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_componente.html', {'form': form})
    
class anyadirPedidoView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        return render(request, 'anyadir_pedido.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_pedido.html', {'form': form})

class anyadirComponenteProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadir_componente_producto.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadir_componente_producto.html', {'form': form})
        
class anyadirPedidoView(View):
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
def detallePedidoView(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'detallePedido.html', {'pedido': pedido})

class detalleComponenteView(View):
    model = Componente
    template_name = 'detalleComponente.html'
    context_object_name = 'componente'
    
class detalleClienteView(View):
    model = Cliente
    template_name = 'detalleCliente.html'
    context_object_name = 'cliente'

class detalleProductoView(View):
    model = Producto
    template_name = 'detalleProducto.html'
    context_object_name = 'producto'

'''class VerPedidoClienteView(View):
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
        

'''

class eliminarProductoView(DeleteView):
    model = Producto  
    template_name = 'borrarProducto.html'  
    success_url = reverse_lazy('base') 
    
class eliminarComponenteView(DeleteView):
    model = Componente  
    template_name = 'borrarComponente.html'  
    success_url = reverse_lazy('base')
    
class eliminarClienteView(DeleteView):
    model = Cliente  
    template_name = 'borrarCliente.html'  
    success_url = reverse_lazy('base')
    
class eliminarPedidoView(DeleteView):
    model = Pedido
    template_name = 'borrarPedido.html'
    success_url = reverse_lazy('base')
    
class modificarProductoView(UpdateView):
        model = Producto
        template_name = 'modificarProducto.html'
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'pdf']
        success_url = reverse_lazy('listaProducto')

class modificarComponenteView(UpdateView):
        model = Componente
        template_name = 'modificarComponente.html'
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'pdf']
        success_url = reverse_lazy('listaComponente')
        
class modificarClienteView(UpdateView):
        model = Cliente
        template_name = 'modificarCliente.html'
        fields = ['nombre', 'apellidos', 'direccion', 'telefono', 'email']
        success_url = reverse_lazy('listaCliente')
        
class modificarPedidoView(UpdateView):
        model = Pedido
        template_name = 'modificarPedido.html'
        fields = ['referencia', 'fecha', 'cliente', 'producto', 'componente']
        success_url = reverse_lazy('listaPedido')