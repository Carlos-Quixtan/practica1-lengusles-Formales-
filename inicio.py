from cargar import cargar
from cargar import seleccionar
from cargar import cuenta
from cargar import minimo
from cargar import maximo
from cargar import suma

print("Bienvenido a SimpleQL")

while True:

    print("1. Cargar")
    print("2. Seleccionar")
    print("3. Maximo")
    print("4. Minimo")
    print("5. Suma")
    print("6. Cuenta")
    print("7. Reportar")
    print("8. Salir")

    datoIngresado = int(input("Ingresa el numero que desea utiizar: "))

    if datoIngresado ==1:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de cargar")
       
        cargar()  # llamo a la funcion cargar y la ejecuto
        print("Los archivos fueron cargados con exito a la memoria! ")
        print("-----------------------------------------------------------------------------------------------------------------")
      

    elif datoIngresado ==2:
        print("------------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de seleccionar")
        
        seleccionar()  # llamo a la seleccionar cargar y la ejecuto
        print("-------------------------------------------------------------------------------------------------------------------")
        

    elif datoIngresado ==3:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de maximo")
        
        maximo()
        print("-----------------------------------------------------------------------------------------------------------------")
      

    elif datoIngresado ==4:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de minimo")
        
        minimo()
        print("-----------------------------------------------------------------------------------------------------------------")
      

    elif datoIngresado ==5:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de suma")
        
        suma()
        print("-----------------------------------------------------------------------------------------------------------------")
     

    elif datoIngresado ==6:

        print("-------------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de contar")
        
        cuenta()   # llamo a la funcion cuenta y la ejecuto

        print("-------------------------------------------------------------------------------------------------------------------")


    elif datoIngresado ==7:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Usted ha escogido la opcion de reportar")
        print("-----------------------------------------------------------------------------------------------------------------")
        
      
    elif datoIngresado == 8:
        print("Gracias por usar nuestro programa, vuelve pronto")
        break
    
    else:
        print("Sellecione un dato correcto para avanzar")
    











    