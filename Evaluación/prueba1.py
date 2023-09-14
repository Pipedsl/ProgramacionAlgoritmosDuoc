import numpy as np
def isNum():
    while(True):
        try:
            x=input()
            x=int(x)
            break
        except:
            print("Error, se esperaba un número, reintente")
    return(x)
def showMenu():
    print("SERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("----------------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Buscar Ficha por Rut")
    print("3) Buscar Medicamentos por Rut")
    print("4) Eliminar Ficha del Paciente")
    print("5) Listar Pacientes Atendidos")
    print("6) Salir")
def isRut():
    while(True):
        x=input()
        if x=="":
            print("Error, campo ingresado vacío, reintente")
        else:
            break
    return(x)

def showPatient(i,j):
    if j==0:
        print("Nombre:",pac[i,j])
    elif j==1:
        print("Rut:",pac[i,j])
    elif j==2:
        print("Edad:",pac[i,j])
    elif j==3:
        print("Sexo:",pac[i,j])
    elif j==4:
        print("Fono:",pac[i,j])
    elif j==5:
        print("Diagnóstico:")
        print(pac[i,j])


pac=np.empty([50,7],dtype="object")
f=0
while(True):
    showMenu()
    opt=isNum()
    if opt==1:
        for i in range(0,7):
            if i==0:
                print("Ingrese el nombre del paciente")
                pac[f,i]=input()
            elif i==1:
                print("Ingrese el rut del paciente")
                pac[f,i]=isRut()
            elif i==2:
                print("Ingrese la edad del paciente")
                pac[f,i]=input()
            elif i==3:
                print("Ingrese el sexo del paciente")
                pac[f,i]=input()
            elif i==4:
                print("Ingrese el fono del paciente")
                pac[f,i]=input()
            elif i==5:
                print("Ingrese el diagnóstico del paciente")
                pac[f,i]=input()
            elif i==6:
                print("Ingrese medicamentos recetados del paciente")
                pac[f,i]=input()
        f+=1
        print("Paciente ingresado con éxito")
    elif opt==2:
        print("Ingrese el rut del paciente a buscar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                print("Paciente encontrado, sus datos son los siguientes:")
                for j in range(0,6):
                    showPatient(i,j)
                 
                break
        else:
            print("Paciente no encontrado")
    elif opt==3:
        print("Ingrese el rut del paciente a buscar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                print("Paciente encontrado, los medicamentos recetados son los siguientes:")
                print(pac[i,6])
                break
        else:
            print("Paciente no encontrado")
    elif opt==4:
        print("Ingrese el rut del paciente a eliminar")
        x=input()
        for i in range(0,50):
            if x==pac[i,1]:
                pac=np.delete(pac,i, axis=0)
                print("Paciente eliminado con éxito")
                break
        else:
            print("Paciente no encontrado")
    elif opt==5:
        for i in range(0,f):
            print("Paciente:")
            for j in range(0,6):
                showPatient(i,j)
    elif opt==6:
        break
    else:
        print("Error, ingrese opción válida")