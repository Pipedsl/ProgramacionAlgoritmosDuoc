import signal
from winsound import SND_PURGE
import numpy as np
from collections import deque
from controlador import sdodb
from controlador.sdodb import ListasNp
from modelo.Persona import Persona
from modelo.Depto import Departamento

#CTLR+C
def handler(signum, frame):
    print(f"{sdodb.bcolors.OKCYAN}Saliendo...{sdodb.bcolors.ENDC}")
    exit(1)
signal.signal(signal.SIGINT, handler)

def imprimirMenu():
    while True:
        try:
            print(f"\n{sdodb.bcolors.HEADER}---Menu---{sdodb.bcolors.ENDC}\n")
            print(f"1.-\t{sdodb.bcolors.OKGREEN}Comprar Departamento{sdodb.bcolors.ENDC}")
            print(f"2.-\t{sdodb.bcolors.OKGREEN}Mostrar departamentos disponibles{sdodb.bcolors.ENDC}")
            print(f"3.-\t{sdodb.bcolors.OKGREEN}Ver listado de compradores{sdodb.bcolors.ENDC}")
            print(f"4.-\t{sdodb.bcolors.OKGREEN}Salir\n{sdodb.bcolors.ENDC}")
            print(f"{sdodb.bcolors.OKCYAN}Selecciona alguna de las siguientes opciones{sdodb.bcolors.ENDC}")
            op = int(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
            if op != 0 or op != None:
                if op == 1:
                    comprarDep()
                if op == 2:
                    mostrarDep()
                if op == 3:
                    mostrarCompradores()
                if op == 4:
                    print(f"{sdodb.bcolors.OKCYAN}Saliendo...{sdodb.bcolors.ENDC}")
                    exit(1)
            else:
                print("Debes ingresar un valor válido para las opciones desplegadas")
        except Exception as err:
            print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")

def comprarDep():
    while True:
        try:
            mostrarTodoDepto() , print("\n")
            print(f"{sdodb.bcolors.HEADER}Estos son los dptos disponibles.¿Te gustaría reservar alguno? Si-No{sdodb.bcolors.ENDC}")
            op = str(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
            op = op.lower()
            if op == "si" or op == "s":
                print(f"{sdodb.bcolors.OKCYAN}¿En qué piso te gustaría arrendar?{sdodb.bcolors.ENDC}\n")
                piso = int(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                print(f"{sdodb.bcolors.OKCYAN}¿En qué dpto.?{sdodb.bcolors.ENDC}\n")
                tipo = str(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                tipo = tipo.upper()
                row, col = calculaDepto(piso, tipo)
                print(f"{sdodb.bcolors.OKCYAN}Indicanos tu RUT (Sin puntos, guión y código verificador.){sdodb.bcolors.ENDC}\n")
                rut = int(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                print(f"{sdodb.bcolors.OKCYAN}Ahora tu Nombre{sdodb.bcolors.ENDC}\n")
                nombre = str(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                print(f"{sdodb.bcolors.OKCYAN}Por último tu Apellido{sdodb.bcolors.ENDC}\n")
                apellido = str(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                print("\n")
                piso = str(piso)
                dpto = piso+tipo
                print(f"{sdodb.bcolors.WARNING}{nombre}, ¿Estás segur@ que quieres reservar el departamento {dpto}?{sdodb.bcolors.ENDC}")
                print(f"{sdodb.bcolors.OKCYAN}Para confirmar vuelve a ingresar su Rut{sdodb.bcolors.ENDC}")
                rrut = int(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                if rut == rrut:
                    newPersona = Persona(rut, nombre, apellido, dpto)
                    newDepto = Departamento(int(piso), tipo, True)
                    sdodb.rellenarCampoArrDepto(row, col, ListasNp.arrDeptos)
                    if sdodb.rellenarFilaArr(newPersona, ListasNp.arrPersonas) == True and sdodb.rellenarFilaArr(newDepto, ListasNp.arrDeptosComprados) == True:
                        break
                else:
                    print(f"{sdodb.bcolors.OKCYAN}Volviendo...{sdodb.bcolors.ENDC}")
                    imprimirMenu()
            elif op == "no" or op == "n":
                print(f"{sdodb.bcolors.OKCYAN}Volviendo...{sdodb.bcolors.ENDC}")
                imprimirMenu()
            else:
                print(f"{sdodb.bcolors.FAIL}Escribe Si o No. Vuelve a intentarlo. No es tan difícil.{sdodb.bcolors.ENDC}")
        except Exception as err:
            ListasNp.arrDeptos[row][col] = None
            sdodb.vaciarFilaArr(rut, ListasNp.arrPersonas)
            print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")

def mostrarDep():
    while True:
        try:
            print(f"\n{sdodb.bcolors().HEADER}¿Deseas imprimir sólo los departamentos existentes?{sdodb.bcolors().ENDC}")
            print(f"{sdodb.bcolors().HEADER}Si - Mostrará sólo los departamentos con reserva. No - Desplegará todo incluyendo los espacios disponibles{sdodb.bcolors().ENDC}\n")
            op = str(input(f"{sdodb.bcolors().OKGREEN}---->\t{sdodb.bcolors().ENDC}"))
            print("\n")
            op = op.lower()
            rows, cols = ListasNp.arrDeptos.shape
            dptos = ""
            ldptos = []
            piso, tipo = None , None
            if op == "si" or op == "s":
                newlis = deque()
                for i in range(rows):
                    for j in range(cols):
                        if ListasNp.arrDeptos[i][j] != None:
                            piso, tipo = sdodb.conversionDepto(i,j)
                            newlis.append(str(piso)+tipo+" "+sdodb.extraerCampoArr(ListasNp.arrDeptos[i][j], ListasNp.arrDeptos, False))

                rs = np.array(newlis, dtype=object)
                cont = 1
                for i in rs:
                    print(f"{sdodb.bcolors().OKGREEN}{cont}.- {i}{sdodb.bcolors().ENDC}")
                    cont = cont + 1
                break
            elif op == "no" or op == "n":
                cont = 10
                print(f"{sdodb.bcolors.HEADER}\t     A\t     B\t       C\t D{sdodb.bcolors.ENDC}")
                for i in range(rows):
                    ldptos = []
                    for j in range(cols):
                        dptos = ListasNp.arrDeptos[i][j]
                        #print(f"{sdodb.bcolors().OKGREEN}{ListasNp.arrDeptos[i][j]}{sdodb.bcolors().ENDC}")
                        if ListasNp.arrDeptos[i][j] == None:
                            ldptos.append("Disp")
                        else:
                            ldptos.append(dptos)
                        if j == 3:
                            print(f"{sdodb.bcolors().OKGREEN}Piso {cont} - {ldptos}{sdodb.bcolors.ENDC}")
                    cont = cont - 1
                break
            else:
                print(f"{sdodb.bcolors.FAIL}Escribe Si o No. Vuelve a intentarlo. No es tan difícil.{sdodb.bcolors.ENDC}")
        except Exception as err:
            print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")

def mostrarCompradores():
    while True:
        try:
            print(f"{sdodb.bcolors.HEADER}¿Deseas verlos a todos? Si-No{sdodb.bcolors.ENDC}\n")
            op = str(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
            op = op.lower()
            if op == "si" or op == "s":
                print(ListasNp.arrPersonas)
                break
            elif op == "no" or op == "n":
                print(f"{sdodb.bcolors.OKCYAN}Ingrese el rut del comprador que deseas buscar{sdodb.bcolors.ENDC}")
                rut = int(input(f"{sdodb.bcolors.HEADER}---->\t{sdodb.bcolors.ENDC}"))
                lista = sdodb.extraerFilaArr(rut, ListasNp.arrPersonas, True)
                if lista[1] != None:
                    print(f"{sdodb.bcolors().HEADER}\n---Imprimiendo---\n{sdodb.bcolors().ENDC}")
                    print(f"{sdodb.bcolors().OKGREEN}Rut:\t\t{lista[0]}{sdodb.bcolors().ENDC}")
                    print(f"{sdodb.bcolors().OKGREEN}Nombre:\t\t{lista[1]}{sdodb.bcolors().ENDC}")
                    print(f"{sdodb.bcolors().OKGREEN}Apellido:\t{lista[2]}{sdodb.bcolors().ENDC}")
                    print(f"{sdodb.bcolors().OKGREEN}Depto:\t\t{lista[3]}{sdodb.bcolors().ENDC}")
                    break
            else:
                print(f"{sdodb.bcolors.FAIL}Escribe Si o No. Vuelve a intentarlo. No es tan difícil.{sdodb.bcolors.ENDC}")
        except Exception as err:
            print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")

def mostrarTodoDepto():
    try:
        rows, cols = ListasNp.arrDeptos.shape
        dptos = ""
        ldptos = []
        cont = 10
        print(f"{sdodb.bcolors.HEADER}\t     A\t     B\t       C\t D{sdodb.bcolors.ENDC}")
        for i in range(rows):
            ldptos = []
            for j in range(cols):
                dptos = ListasNp.arrDeptos[i][j]
                if ListasNp.arrDeptos[i][j] == None:
                    ldptos.append("Disp")
                else:
                    ldptos.append(dptos)
                if j == 3:
                    print(f"{sdodb.bcolors().OKGREEN}Piso {cont} - {ldptos}{sdodb.bcolors.ENDC}")
            cont = cont - 1
            if i == 9:
                break
    except Exception as err:
        print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")

def calculaDepto(piso, tipo):
    try:
        if piso == 10: row = 0
        if piso == 9: row = 1
        if piso == 8: row = 2
        if piso == 7: row = 3
        if piso == 6: row = 4
        if piso == 5: row = 5
        if piso == 4: row = 6
        if piso == 3: row = 7
        if piso == 2: row = 8
        if piso == 1: row = 9
        if tipo == "A": col = 0
        if tipo == "B": col = 1
        if tipo == "C": col = 2
        if tipo == "D": col = 3
        return row, col
    except Exception as err:
        print(f"{sdodb.bcolors.WARNING}Ha ocurrido un error. Razón: {sdodb.bcolors.FAIL}[{sdodb.bcolors.ENDC}",str(err),f"{sdodb.bcolors.FAIL}]{sdodb.bcolors.ENDC}")


if __name__ == '__main__':
    imprimirMenu()