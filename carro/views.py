from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect



def agregar_producto(req, producto_id):

    carro = Carro(req)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    req.session["carro"] = carro.carro
    return redirect("Tienda")


def eliminar_producto(req, producto_id):

    carro = Carro(req)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)

    return redirect("Tienda")


def restar_producto(req, producto_id):

    carro = Carro(req)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)

    return redirect("Tienda")


def limpiar_carro(req):

    carro = Carro(req)
    if 'carro' not in req.session:
        req.session['carro'] = {}
    carro.limpiar_Carro()

    return redirect("Tienda")

