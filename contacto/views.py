from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def contacto(req):
    data= {
        'form': ContactoForm()
    }
    if req.method == 'POST':
        formulario= ContactoForm(data=req.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "formulario enviado"
        else:
            data["form"] = formulario   

    return render(req, "contacto.html",data)

