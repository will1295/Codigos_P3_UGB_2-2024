import pdb
import sys
while True:
    try:
        def dividir(num1,num2):
            total = num1/num2
            return total
        num1 = int(input("Escribe un número: "))
        num2 = int(input("Escribe otro número: "))
        print(dividir(num1,num2))
        op = input("¿Desea hacer otra división? (s/n)").lower()
        if(op=="s"):
            continue
        elif(op=="n"):
            break
        else:
            print("Error operación no valida")
            #break      
    except:
        print("Error no se puede dividir entre cero")
        #break
        #pdb.post_mortem(sys.exc_info()[2])
        

