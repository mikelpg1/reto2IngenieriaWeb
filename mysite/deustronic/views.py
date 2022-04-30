from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pagPrincipal.html')

def pedidos(request):
    return render(request, 'gestionar_pedidos.html')

def catalogo(request):
    return render(request, 'ver_catalogo.html')

def contacto(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def singup(request):
    return render(request, 'singup.html')
