import sys

print("Uso de modulo sys")
#break
#sys.exit()
#print("Fin del programa")

print("Version de Python: ",sys.version)
print("Sistema: ",sys.platform)

print("Escribe algo: ")
palabra = sys.stdin.readline().strip()
print(palabra)