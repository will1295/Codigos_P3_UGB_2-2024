import sys

#print("Hello world")
#sys.exit("Se ha encontrado un error")
#print("CODIGO")

#sys.stdin()
print("Escribe tu nombre: ")
nombre = sys.stdin.readline()
print(f"Hola {nombre}")

#sys.stdout()
numero = input("Escribe un numero: ")
sys.stdout.write(f"Tu numero es el: {numero}")
#sys.stderr()

try:
    print(2/0)
except:
    sys.stderr.write("No se puede dividir entre cero")

print(sys.modules['sys'])