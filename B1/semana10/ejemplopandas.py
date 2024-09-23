import pandas as pd

datos = {
    'Nombre':["Juan","Pedro","Luis","Ana"],
    'Edad':[30,31,45,32],
    'Municipio':["San Miguel","Usulutan","La Union","San Salvador"],
    'Puesto':["Empleado","Empleado","Ordenanza","Gerente"]
}

df = pd.DataFrame(datos)
print(df)