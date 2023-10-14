


def importe_del_carro(req):
    total = 0
    if req.user.is_authenticated:
        for key, value in req.session["carro"].items():
            total = total+(float(value["precio"])*value["cantidad"])
    return {"importe_del_carro": total}
