def area(base,altura):
    resultado = (base*altura)/2
    return resultado
while True:
    try:
        altura = int(input("Escriba el valor de la altura: "))
        base = int(input("Escriba el valor de la base: "))
        print(area(base,altura))
        #break
    except:
        print("Error, valor inválido")
    finally:
        op = input("¿Deseas intentar otra vez? (s/n)")
        if(op.lower()=="n"):
            break
        else:
            continue
