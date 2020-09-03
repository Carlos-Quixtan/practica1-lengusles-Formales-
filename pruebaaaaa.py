import json



datos = input("ingrese dato " )
print(datos)

variable_cargar =input("CARGAR ")
variable_lista = [variable_cargar]

#print(datos,datos1)

file = open(variable_cargar)
data = json.load(file)
file.close()
#print(data) # esta linea sirve para imprimir lo que tiene cada archivo


