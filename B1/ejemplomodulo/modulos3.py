import os

#os.mkdir("nueva_carpeta")
#os.makedirs("nueva_carpeta/subcapeta")
carpeta = "nueva_carpeta"
#Para verificar si la direccion existe
if(os.path.exists(carpeta)):
    #Para verificar si es un directorio
    if(os.path.isdir(carpeta)):
        print("El directorio ya existe")
else:
    os.mkdir("nueva_carpeta")
archivo = "mi_archivo.txt"
ruta = os.path.join(carpeta,archivo)
with open(ruta,'w') as f:
    f.write("Hola Python")


