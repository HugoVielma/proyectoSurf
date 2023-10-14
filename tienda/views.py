from django.shortcuts import render
from .models import Producto
# Create your views here.
def tienda(req):
    productos=Producto.objects.all()
    return render(req,"tienda.html", {"productos":productos})