import numpy as np

def esnum():
    while(True):
        try:
            x=input()
            x=int(x)
            break
        except:
            print("Error, se esperaba un número, reintente")
    return(x)
def showMenu():
    print("Auto Seguro")
    print("----------------------------------------")
    print("1) Grabar:")
    print("2) Buscar:")
    print("3) Imprimir certificado:")
    print("4) Salir.")
def showvehiculo(i,j):
    if j==0:
        print("Tipo:",auto[i,j])
    elif j==1:
        print("Patente:",auto[i,j])
    elif j==2:
        print("Marca:",auto[i,j])
    elif j==3:
        print("Precio:",auto[i,j])
    elif j==4:
        print("Cantidad multas:",auto[i,j])
    elif j==5:
        print("Fecha multa:",auto[i,j])
    elif j==6:
        print("Monto multa: $",auto[i,j])
    elif j==7:
        print("Fecha de registro:",auto[i,j])
    elif j==8:
        print("Nombre propietario:",auto[i,j])
def espatente():
    while(True):
        x=input()
        if x=="":
            print("Error, campo ingresado vacío, reintente")
        else:
            break
    return(x)
def esprecio():
    while(True):
        x=int(input())
        if x < 5000000:
            print("Error, el precio debe ser mayor a $5000000")
        else:
            break
    return(x)

auto=np.empty([50,9],dtype="object")
f=0
while(True):
    showMenu()
    opt=esnum()
    if opt==1:
        for i in range(0,9):
            if i==0:
                print("Ingrese el Tipo de vehiculo")
                auto[f,i]=input()
            elif i==1:
                print("Ingrese la patente del vehiculo")
                auto[f,i]=espatente()
            elif i == 2:
                print("Ingrese la marca del vehiculo")
                auto[f,i]=input()
            elif i == 3:
                print("Ingrese el precio del vehiculo")
                auto[f,i]=esprecio()
            elif i == 4:
                print("Ingrese cantidad de multas")
                auto[f,i]=input()
            elif i == 5:
                print("Ingrese fecha de multa")
                auto[f,i]=input()
            elif i == 6:
                print("Ingrese monto total de multas")
                auto[f,i]= int(input())
            elif i == 7:
                print("Ingrese fecha registro del vehiculo")
                auto[f,i]=input()
            elif i == 8:
                print("Ingrese nombre del propietario")
                auto[f,i] = input()       
        f+=1
        print("\nDatos del Vehiculo ingresados con exito\n")

    elif opt == 2:
        print("Ingrese patente del vehiculo: ")
        x = input()
        for i in range(0,50):
            if x == auto[i,1]:
                print("Vehiculo encontrado, sus datos son los siguientes:\n")
                for j in range(0,9):
                    showvehiculo(i,j)

                break
        else:
            print("vehiculo no encontrado")
    elif opt==3:
        print("Ingrese la patente del vehiculo")
        x=input()
        for i in range(0,50):
            if x==auto[i,1]:
                print("vehiculo encontrado")
                print("----------------------------------------")
                print("Certificado de anotaciones vigentes:")
                for j in range(0,9):
                    if j == 1:
                        print("Patente:",auto[i,j])
                    if j == 8:
                        print("Nombre propietario:",auto[i,j])
                print("----------------------------------------")
                break
            else:
                print("Vehiculo no encontrado")
    elif opt==4:
        print("Gracias por ingresar a Auto Seguro, Autosegurov1.0 es un programa creado por HugoNavarrete")
        break
    else:
        print("Error, ingrese opción válida")