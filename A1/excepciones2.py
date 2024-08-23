import pdb
class miexcepcion(Exception):
    def __init__(self,mensaje): 
         super().__init__(mensaje)
         self.mensaje = mensaje
         

    #Llamar este metodo cuando se hace el return
    #def __str__(self):
    #    return {f"Error: {self.mensaje}"}


while True:
    try:
        def dividir(num1,num2):
            total = num1/num2
            if(num2==0):
                raise miexcepcion("No se puede dividir entre cero")
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
            break      
    except:
        #pdb.set_trace()
        print(miexcepcion("Error aquí"))
