#import modulo
#from modulo import hacer_pizza,datoscli,sucursal
from modulo import hacer_pizza as hp
from modulo import datoscli as dc
from modulo import sucursal as s

print(f"Sucursal de {s}")
hp("Familiar","Champiñones","Pepperoni","Queso","Piña")
hp("Personal","Jamon","Queso")
dc("San Miguel","Pepito",14512632)

"""
Crear un modulo que tenga las siguientes funciones y que
luego las utilice en un archivo principal.

1-Volumen de un cilindro
2-Volumen de una esfera
3-Volumen de un cono
"""