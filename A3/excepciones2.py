#compras, la cantidad de productos no puede ser negativos
class prodnegativo(Exception):
    #"No se puede llegar cantidades negativas"
    pass

def compra(cantidad,precio):
    total = cantidad*precio
    return total

#compra(20,10)
while True:
    tcompra = 0
    #total = cantidad*precio
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if(cantidad<=0):
            raise prodnegativo
    except prodnegativo:
        print("Error en la cantidad")
        break
    precio = int(input("Ingrese el precio del producto: "))
    tcompra = compra(cantidad,precio)
    print(tcompra)
    op = input("¿Desea escanear otro producto? (s/n)")
    if(op.lower == "n"):
        break
    else:
        tcompra+=tcompra
        continue