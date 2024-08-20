import pdb
#Funcion que hace una division
def div(num1,num2):
    return  num1/num2

#Define la funcion principal del programa
def main():
    n1 = 10
    n2 = 0
    try:
        resultado = div(n1,n2)
        print(f"El resultado es p {resultado}")
    except Exception:
       pdb.post_mortem()
        

#Llamando a la funcion principal
if __name__=="__main__":
    main()

