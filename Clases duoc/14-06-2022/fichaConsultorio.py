import numpy as np
def isNum(): #
    while(True):
        try:
            x = input()
            x = int(x)
            break
        except:
            print("Erorr, se esperaba un número, reintente")
    return (x)
def showMenu():
    print("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("----------------------------------------")
    print("1) INGRESAR FICHA DEL PACIENTE")
    print("2) BUSCAR FICHA POR RUT")
    print("3) BUSCAR MEDICAMENTOS POR RUT")
    print("4) ELIMINAR FICHA DEL PACIENTE")
    print("5) LISTAR PACIENTES ATENDIDOS")
    print("6) SALIR")
def isRut():
    while (True):
        x = input()
        if x == "":
            print("Error, campo ingresado vacio, reintente")
        else:
            break
    return (x)

def showPatient(i,j):
    if j == 0:
        print("Nombre:",pac[i,j])


pac=np.empty([50,7],dtype="object")
f = 0
while (True):
    showMenu()
    opt = isNum()
    if opt == 1:
        for i in range (0,7):
            if i == 0:
                print("Ingrese el nombre del paciente")
                pac[f,i] = input()
            elif i == 1:
                print("Ingrese el rut del paciente")
                pac[f,i] = isRut()
            elif i == 2:
                print("Ingrese la edad del paciente")
                pac[f,i] =input()
            
        f+=1
        print("Paciente ingresado con exito")
    elif opt ==2:
        print("Ingrese el rut del paciente a buscar")
        x = input()
        for i in range (0,50):
            if x == pac[i,1]:
                print("Paciente encontrado sus datos son los siguientes")
                for j in range (0,6):
                    showPatient(i,j)
                
                break
        else:
            print("Paciente no encontrado")
    
    elif opt == 3:
        print("__")
    
    elif opt == 4:
        print("Ingrese el rut del paciente que quiere eliminar")
        x = input()
        for i in range(0,50):
            pac = np.delete(pac,i, axis=0)
            print("Paciente eliminado con éxito")


    elif opt == 5:
        for i in range (0,f):
            print("Paciente:")
            for j in range(0,6):
                showPatient(i,j)
    elif opt == 6:
        break
    else:
        print("Error, ingrese opción valida")

    _
