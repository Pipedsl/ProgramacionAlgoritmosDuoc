import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def rellenarFilaArr(obj, arr):
    obj = list(obj.__dict__.values())
    row, col = arr.shape
    agregado = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == None:
                arr[i] = obj
                print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER}[Agregado]{bcolors().OKCYAN} {obj} {bcolors().HEADER}[Agregado]{bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                agregado = True
                return agregado
            else:
                break
        if agregado == True:
            return agregado

def rellenarCampoArrDepto(fila, columna, arr):
    arr[fila][columna] = "No Disp"
    piso, tipo = conversionDepto(fila, columna)
    piso = str(piso)
    dpto = piso+tipo
    print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER}[Agregado]{bcolors().OKCYAN} {dpto} {bcolors().HEADER}[Agregado]{bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")

def conversionDepto(fila, columna):
    if fila == 0: piso = 10
    if fila == 1: piso = 9
    if fila == 2: piso = 8
    if fila == 3: piso = 7
    if fila == 4: piso = 6
    if fila == 5: piso = 5
    if fila == 6: piso = 4
    if fila == 7: piso = 3
    if fila == 8: piso = 2
    if fila == 9: piso = 1
    if columna == 0: tipo = "A"
    if columna == 1: tipo = "B"
    if columna == 2: tipo = "C"
    if columna == 3: tipo = "D"
    return piso, tipo

def vaciarFilaArr(value, arr):
    row, col = arr.shape
    obj = np.empty([col],dtype=object)
    vaciado = False
    for i in range(row):
        for j in range(col):
            print(arr[i][j])
            if arr[i][j] == value:
                arr = np.delete(arr, i, 0)
                print(
                    f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER}[Eliminado]{bcolors().OKCYAN} {value} {bcolors().HEADER}[Eliminado]{bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                vaciado = True
                return arr
                break
        if vaciado == True:
            break

def filter_where(arr, value):
    return arr[np.where(arr == value)]

def extraerFilaArr(value, arr, mssg):
    row, col = arr.shape
    obj = []
    extraido = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == value:
                obj = arr[i]
                if mssg == True:
                    print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER} [Extraido]{bcolors().OKCYAN} {obj} {bcolors().HEADER}[Extraido] {bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                extraido = True
                break
        if extraido == True:
            break
    return obj

def extraerCampoArr(value, arr, mssg):
    row, col = arr.shape
    obj = []
    extraido = False
    for i in range(row):
        for j in range(col):
            if arr[i][j] == value:
                obj = arr[i][j]
                if mssg == True:
                    print(f"{bcolors().OKGREEN}[✓]{bcolors().FAIL} [SDODB]{bcolors().HEADER} [Extraido]{bcolors().OKCYAN} {obj} {bcolors().HEADER}[Extraido] {bcolors().FAIL}[SDODB] {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
                extraido = True
                break
        if extraido == True:
            break
    return obj

class ListasNp:
#Variables Globales - Todas las listas que se deban inicializar
    arrDeptos = np.empty([10, 4], dtype=object)
    arrDeptosComprados = np.empty([40, 3], dtype=object)
    arrPersonas = np.empty([40, 4], dtype=object)
#Ejemplos
    arrDeptos[0][2] = "No disp"
    arrPersonas[0] = [19323450, "Martin", "Rojas", "10C"]
    arrDeptosComprados[0] = [10, "C", True]
    

    def __init__(self):
        self.arrDeptos = self.arrDeptos
        self.arrPersonas = self.arrPersonas
        
#Set - Get Arreglos de Departamentos
    def setArrDeptos(self, arr):
        self.arrDeptos = arr
    
    def getArrDeptos(self):
        return self.arrDeptos

#Set - Get Arreglos de Personas
    def setArrPersonas(self, arr):
        self.arrPersonas = arr

    def getArrPersonas(self):
        return self.arrPersonas 