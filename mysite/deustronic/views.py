from sre_constants import SUCCESS
from django.shortcuts import get_list_or_404, redirect, render
from django.views import View
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.conf import settings
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.
def inicio(request):
    componente = get_list_or_404(Componente.objects.order_by('componente_nombre'));
    producto = get_list_or_404(Producto.objects.order_by('producto_nombre'));
    cliente = get_list_or_404(Cliente.objects.order_by('cliente_nombreEmpresa'));
    pedido = get_list_or_404(Pedido.objects.order_by('pedido_referencia'));
    
    context = {
        'componentes': componente,
        'productos': producto,
        'clientes': cliente,
        'pedidos': pedido,
    }
    return render(request, 'pagPrincipal.html', context)

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

# AÑADIR PRODUCTO #
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
    

# AÑADIR COMPONENTE #
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
    
# AÑADIR PEDIDO #
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
class detallePedidoView(View):
    model = Pedido
    template_name = 'detallePedido.html'
    context_object_name = 'pedido'


# VER COMPONENTE #
class detalleComponenteView(View):
    model = Componente
    template_name = 'detalleComponente.html'
    context_object_name = 'componente'
    
# VER CLIENTE #
class detalleClienteView(View):
    model = Cliente
    template_name = 'detalleCliente.html'
    context_object_name = 'cliente'

# VER PRODUCTO #
class detalleProductoView(View):
    model = Producto
    template_name = 'detalleProducto.html'
    context_object_name = 'producto'

# VER PEDIDO CLIENTE #
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
    
class updateProductoView(UpdateView):
        model = Producto
        template_name = 'updateProducto.html'
        fields = ['producto_nombre', 'producto_descripcion', 'producto_categoria', 'producto_precio', 'producto_pdf']
        success_url = reverse_lazy('listaProducto')

class updateComponenteView(UpdateView):
        model = Componente
        template_name = 'updateComponente.html'
        fields = ['componente_nombre', 'componente_descripcion', 'componente_categoria', 'componente_precio', 'componente_pdf']
        success_url = reverse_lazy('listaComponente')
        
class updateClienteView(UpdateView):
        model = Cliente
        template_name = 'updateCliente.html'
        fields = ['cliente_nombre', 'cliente_apellidos', 'cliente_direccion', 'cliente_telefono', 'cliente_email']
        success_url = reverse_lazy('listaCliente')
        
class updatePedidoView(UpdateView):
        model = Pedido
        template_name = 'updatePedido.html'
        fields = ['pedido_referencia', 'pedido_fecha', 'pedido_cliente', 'pedido_producto', 'pedido_componente']
        success_url = reverse_lazy('listaPedido')