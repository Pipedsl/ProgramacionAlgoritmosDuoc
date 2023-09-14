import numpy as np

def showedificio():
    print(piso1)
    print(piso2)
    print(piso3)
    print(piso4)
    print(piso5)
    print(piso6)
    print(piso7)
    print(piso8)
    print(piso9)
    print(piso10)

piso1 = ["A","B","C","D"]
piso2 = ["A","B","C","D"]
piso3 = ["A","B","C","D"]
piso4 = ["A","B","C","D"]
piso5 = ["A","B","C","D"]
piso6 = ["A","B","C","D"]
piso7 = ["A","B","C","D"]
piso8 = ["A","B","C","D"]
piso9 = ["A","B","C","D"]
piso10 = ["A","B","C","D"]

print("Ingrese el numero de piso que le interesa:")
reserva = int(input())
if reserva == 1:
    print("Eligio el piso numero 1, elija el departamento que desea: A,B,C o D")
    tipo = input()
    if tipo == "A":
        print("Usted selecciono el departamento 1A")
        if piso1[0] == "A":
            print("Departamento disponible")
            piso1[0] = "X"
        else:
            print("Departamento vendido")
    if tipo =="B":
        print("Usted selecciono el departamento 1B")
        if piso1[1] == "B":
            print("Departamento disponible")
            piso1[1] = "X"
        else:
            print("Departamento vendido")
    if tipo =="C":
        print("Usted selecciono el departamento 1C")
        if piso1[2] == "C":
            print("Departamento disponible")
            piso1[2] = "X"
        else:
            print("Departamento vendido")
    if tipo =="D":
        print("Usted selecciono el departamento 1D")
        if piso1[3] == "D":
            print("Departamento disponible")
            piso1[3] = "X"
        else:
            print("Departamento vendido")

showedificio()

