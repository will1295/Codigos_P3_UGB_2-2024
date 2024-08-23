def potencia(num,pot):
    return num**pot

while True: 
    try: 
        num = int(input("Ingrese un número: "))
        pot = int(input("Ingrese a que número va elevado: "))
        print(potencia(num,pot))
    except:
        print("Ingrese porfavor solo números: ")
    finally:
        op = input("¿Desea intentarlo de nuevo? (s/n)")
        if(op=="n"):
            break
        else:
            continue

