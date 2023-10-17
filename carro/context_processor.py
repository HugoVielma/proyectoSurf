def importe_del_carro(req):
    total = 0
    if req.user.is_authenticated:
        for key, value in req.session["carro"].items():
            total = total+float(value["precio"])
    else:
        total= "Debes logearte para continuar"
    return {"importe_del_carro": total}
