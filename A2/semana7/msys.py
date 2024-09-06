import sys

print("Hola Mundo")
#sys.exit("Error encontrado, finalizando la ejecución del programa")
#print("¿Como te encuentras?")

print("Ingresa tu nombre: ")
#nombre = sys.stdin.readline()
nombre = sys.stdin.readline().strip()
#print("Hola ",nombre)
sys.stdout.write(f"Hola {nombre}")

try:
    print(4/0)
except:
    sys.stderr.write("No se puede dividir entre cero")
