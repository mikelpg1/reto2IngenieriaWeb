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
        return render(request, 'anyadirCliente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyadirCliente.html', {'form': form})

# AÑADIR PRODUCTO #
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

# AÑADIR COMPONENTE #
class anyadirComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        return render(request, 'anyadirComponente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadirComponente.html', {'form': form})

# AÑADIR PEDIDO #
    
class anyadirPedidoView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        return render(request, 'anyadirPedido.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        return render(request, 'anyaadirPedido.html', {'form': form})

# AÑADIR COMPONENTE PRODUCTO #
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
        
    
# -- VISTAS DE VER --  #

# VER PEDIDO #
def detallePedidoView(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'detallePedido.html', {'pedido': pedido})

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

# -- VISTAS DE ELIMINAR -- #
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
    

# -- VISTAS DE MODIFICAR -- #
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