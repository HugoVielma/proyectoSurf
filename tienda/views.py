from django.shortcuts import render
from .models import Producto
from carro.carro import Carro

def tienda(req):
    productos = Producto.objects.all()

   
    carro = Carro(req)
    contenido_carro = carro.carro
   

    return render(req, "tienda.html", {"productos": productos, "carro_items": contenido_carro})
