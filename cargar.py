from io import open
import json
dataArray = [] # me va servir para guardar todos los datos que el usuario elija ya que una variable no guarda todo
numerosSumEdad = []
numerosSumPromedio=[]
numeros=[]
numerosMinPromedio=[]
numerosMinEdad=[]
numerosMaxPromedio=[]
numerosMaxEdad=[]

def cargar():

    global varCuantosDatosTieneArreglo

    print("Ingrese el nombre de los archivos que desea cargar separados por una coma (,) ")
    print("archivo1")
    print("archivo2")
    print("archivo3")
    print("archivo4")
    print("archivo5")
    print("archivo6")
    print("archivo7")
    print("archivo8")
    print("archivo9")
    print("archivo10")

    datos = input("CARGAR " )
    

    datos_separados= datos.split(', ')  #me separa los datos y mete a un arreglo separado por coma

    varCuantosDatosTieneArreglo = len(datos_separados) # para saber cuantos datos tiene el arreglo y con esto correr while

    primeraPosicion = 0  #para imprmir la posicion cero del arreglo


    while primeraPosicion < varCuantosDatosTieneArreglo:
        #print(datos_separados[primeraPosicion])
        #primeraPosicion = primeraPosicion + 1
        file = open(datos_separados[primeraPosicion])
        #data = json.load(file)

        dataArray.append(json.load(file)) # llamo al data array ya que esto me sirve para guardar el nombre de cada 
                                            # archivo y el appenn para agregar elemntos al array
           
        file.close()
        primeraPosicion =primeraPosicion + 1 # le voy sumando 1 a la posicion del arreglo para poder cargar 
                                                        # todos los datos seleccionados
    return dataArray    # recibo la informacion que la funcion dataArray almacena no solo quiero
                        # que me imprima el estring, yo quiero el dato de la funcion para poder usarlo donde 
                        # yo quiera    
#--------------------------------------------  FUNCION PARA SELECCIONAR ----------------------------------

def seleccionar(): 
    print("1. SELECCIONAR")
    print("2. SELECCIONAR*")
    datoPedido = int(input("ingrese lo que desea " ))

    if datoPedido== 2 :
        for linea in dataArray:
            for obj in linea:
                print(obj)

    elif datoPedido==1:
        datos = input("SELECCIONAR ")   # me sirve para saber que quiere el usuario que le muestre (nom,eda,activ,prom)
        datosSeparadosDeSeleccionar = datos.split(", ")  # separo las claves que en usuario ingreso por como y espacio
                                                     # y los mete a un arreglo 
                                                     
        for linea in dataArray:
            for obj in linea:
                for col in datosSeparadosDeSeleccionar:
                    if col == "nombre": 
                        print(obj["nombre"])
                        continue
                    if col == "edad": 
                        print(obj["edad"])
                        continue
                    if col == "activo":
                        print(obj["activo"])
                        continue
                    if col == "promedio":
                        print(obj["promedio"])
            

#--------------------------------------------  FUNCION PARA CUENTA ----------------------------------

def cuenta ():
    print ("El numero de registros cargados es: " + str(varCuantosDatosTieneArreglo))
    print("-------------------------------------------------------------------------------------------------------------------")

#--------------------------------------------  FUNCION PARA SUMA ----------------------------------      

def suma():
    datosIngresados = input("SUMA ")   # me sirve para saber que quiere el usuario que le muestre (nom,eda,activ,prom)
    datosSeparadosMaximo = [datosIngresados]  # separo las claves que en usuario ingreso por como y espacio
                                                # y los mete a un arreglo
    if datosIngresados == "edad":                                                 
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "edad":

                        numerosSumEdad.append(obj["edad"])  # meto en un array los valores de la clave dada

        print(sum(numerosSumEdad))

    elif datosIngresados=="promedio":
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "promedio":

                        numerosSumPromedio.append(obj["promedio"])

        print(sum(numerosSumPromedio))
    else:
        print("Ingreso un dato erroneo")



#--------------------------------------------  FUNCION PARA MINIMO ----------------------------------  

def minimo():
    datosIngresados = input("MINIMO ")   # me sirve para saber que quiere el usuario que le muestre (nom,eda,activ,prom)
    datosSeparadosMaximo = [datosIngresados]  # separo las claves que en usuario ingreso por como y espacio
                                                # y los mete a un arreglo
    if datosIngresados == "edad":                                                 
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "edad":

                        numerosMinPromedio.append(obj["edad"])  # meto en un array los valores de la clave dada

        print(min(numerosMinPromedio))

    elif datosIngresados=="promedio":
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "promedio":

                        numerosMinEdad.append(obj["promedio"])

        print(min(numerosMinEdad))
    else:
        print("Ingreso un dato erroneo")




#--------------------------------------------  FUNCION PARA MAXIMO ----------------------------------  

def maximo():
    datosIngresados = input("MAXIMO ")   # me sirve para saber que quiere el usuario que le muestre (nom,eda,activ,prom)
    datosSeparadosMaximo = [datosIngresados]  # separo las claves que en usuario ingreso por como y espacio
                                                # y los mete a un arreglo
    if datosIngresados == "edad":                                                 
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "edad":

                        numerosMaxEdad.append(obj["edad"])

        print(max(numerosMaxEdad))

    elif datosIngresados=="promedio":
        for linea in dataArray:
            for obj in linea:
                for posicion in datosSeparadosMaximo:
                    if posicion == "promedio":

                        numerosMaxPromedio.append(obj["promedio"])

        print(max(numerosMaxPromedio))
    else:
        print("Ingreso un dato erroneo")
            


   
                    

