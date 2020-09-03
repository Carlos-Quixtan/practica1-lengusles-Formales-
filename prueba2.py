import json
from io import open 
#print("-------------------------------------------------------------------------------")
#print                    este cogigo es el bueno para cargar multiples archivos
#print("-------------------------------------------------------------------------------")

datos = input("ingrese dato " )

datos_separados= datos.split(', ')  #me separa los datos y mete a un arreglo separado por coma

#print(datos_separados[1])

varCuantosDatosTieneArreglo = len(datos_separados) # para saber cuantos datos tiene el arreglo y con esto correr while

primeraPosicion = 0  #para imprmir la posicion cero del arreglo

while primeraPosicion < varCuantosDatosTieneArreglo:
    #print(datos_separados[primeraPosicion])
    #primeraPosicion = primeraPosicion + 1
    file = open(datos_separados[primeraPosicion])
    data = json.load(file)
    file.close()
    print(data)  #sirve para comprobar que si esta cargando los datos
    primeraPosicion = primeraPosicion + 1 # le voy sumando 1 a la posicion del arreglo para poder cargar 
                                          # todos los datos seleccionados



#variable_cargar =input("CARGAR ")
#variable_lista = [variable_cargar]

#print(datos,datos1)

#file = open(variable_cargar)
#data = json.load(file)
#file.close()