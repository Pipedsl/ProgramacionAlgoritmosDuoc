import numpy as np
fecha = []
print("Ingrese la fecha de hoy:\n1)Ingrese el día\n2)Ingrese mes\n3)Ingrese año")
dia = int(input("1) "))
mes = (input("2) "))
ano = int(input("3) "))
fecha.append(dia)
fecha.append(mes)
fecha.append(ano)
print(f"La fecha de hoy es: {fecha}\n")
fechau = []
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
    print("REGISTRO CIVIL")
    print("----------------------------------------")
    print("1) Ingresar Ficha del Usuario")
    print("2) Buscar Ficha por Rut")
    print("3) Certificados")
    print("4) Salir")
def isRut():
    while(True):
        x=input()
        if x=="":
            print("Error, campo ingresado vacío, reintente")
        else:
            break
    return(x)
def showUsuario(i,j):
    if j==0:
        print("Nombre:",usu[i,j])
    elif j==1:
        print("Rut:",usu[i,j])
    elif j==2:
        print("Fecha de Nacimiento:",usu[i,j])
        if fechau[2] < 2004:
            print("Puede obtener licencia de conducir")
        else:
            print("No puede obtener licencia de conducir")
    elif j==3:
        print(f"Estado Civil: {usu[i,j]}\n")
def showCnacimiento(i,j):
    if j==0:
        print("Nombre:",usu[i,j])
    elif j==1:
        print("Rut:",usu[i,j])
    elif j==2:
        print(f"Fecha de Nacimiento:{usu[i,j]}\n")
def showCantecedentes(i,j):
    if j==0:
        print("Nombre:",usu[i,j])
    elif j==1:
        print("Rut:",usu[i,j])
    elif j==2:
        print(f"Edad:{fecha[2]-fechau[2]}")
    elif j==3:
        print(f"Estado Civil:{usu[i,j]}\n")


usu=np.empty([50,7],dtype="object")
f=0
while(True):
    showMenu()
    opt=isNum()
    if opt==1:
        for i in range(0,7):
            if i==0:
                print("Ingrese el nombre del usuario")
                usu[f,i]=input()
                name = usu[f,i]
            elif i==1:
                print("Ingrese el rut del usuario")
                usu[f,i]=isRut()
            elif i==2:
                print("Ingrese la fecha de nacimiento: \n1)Día\n2)Mes\n3)Año ")
                diau = int(input("1) "))
                mesu = (input("2) "))
                anou = int(input("3) "))
                fechau.append(diau)
                fechau.append(mesu)
                fechau.append(anou)
                usu[f,i]=fechau
            elif i==3:
                print("Ingrese el Estado Civil del usuario")
                usu[f,i]=input()
                ecivil = usu[f,i]
                
        f+=1
        print("Usuario ingresado con éxito\n")
    elif opt == 2:
        print("Ingrese el rut del usuaior: ")
        x = input()
        for i in range(0,50):
            if x == usu[i,1]:
                print("Usuario encontrado, sus datos son los siguientes:\n")
                for j in range(0,6):
                    showUsuario(i,j)

                break
        else:
            print("Usuario no encontrado")
    elif opt==3:
        print("Ingrese el rut del usuario a buscar")
        x=input()
        for i in range(0,50):
            if x==usu[i,1]:
                print("Usuario encontrado, elija el certificado deseado: \n\n1)Certificado de Nacimiento \n2)Certificado de Antecedentes")
                opt2 = int(input())
                if opt2 == 1:
                    print("----------------------------------------")
                    print("\nCertificado de Nacimiento:")
                    for j in range(0,6):
                        showCnacimiento(i,j)
                    print("----------------------------------------")
                    break
        
                elif opt2 == 2:
                    print("----------------------------------------")
                    print("\nCertificado de Antecedentes")
                    for j in range(0,6):
                        showCantecedentes(i,j)
                    print("----------------------------------------")
                    break
            else:
                print("Paciente no encontrado")
    elif opt==4:
        break
    else:
        print("Error, ingrese opción válida")
