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


def correctAttr(attr, typ, attrname, objname): 
    currentType = type(attr)
    try:
        if isinstance(attr, typ):
            return True
        else:
            raise AttributeError()
    except AttributeError:
        print(f"{bcolors().FAIL}[✘]{bcolors().HEADER}[{objname}]{bcolors().FAIL} El atributo '{attrname}' no corresponde al tipo ingresado {attr} ({currentType}). Debe ser una instancia de {typ} {bcolors().HEADER}[{objname}]{bcolors().FAIL}[✘]{bcolors().ENDC}")
        return False

class Departamento:

    def __init__(self, piso, tipo, comprado):
        try:
            if correctAttr(piso, int, attrname='Piso', objname="Departamento"):
                self.piso = piso
            else:
                raise AttributeError
            if correctAttr(tipo, str, attrname='Tipo', objname="Departamento"):
                self.tipo = tipo
            else:
                raise AttributeError
            if correctAttr(comprado, bool, attrname='Comprado', objname="Departamento"):
                self.apellido = comprado
            else:
                raise AttributeError
            print(f"{bcolors().OKGREEN}[✓]{bcolors().ENDC} {bcolors().OKCYAN}{bcolors().HEADER}[Departamento] {bcolors().OKCYAN}Creado correctamente {bcolors().HEADER}[Departamento]{bcolors().ENDC} {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
        except AttributeError as er:
            print(f"{bcolors().FAIL}[✘]{bcolors().HEADER} [Departamento]{bcolors().ENDC} {bcolors().FAIL}No se pudo inicializar Departamento. Comprueba que los datos estén correctamente ingresados{bcolors().FAIL} {bcolors().HEADER}[Departamento] {bcolors().FAIL}[✘]{bcolors().ENDC}")

    def contructor(self):
        self.piso = 0 
        self.tipo = ""
        self.comprado = False

    def imprimirDepto(self):    
        print(f"{bcolors.HEADER}\n --- Informacion del Dpto. {self.piso}|{self.tipo} --- \n")
        print(f"{bcolors.OKGREEN}Piso:\t{self.piso}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Tipo:\t{self.tipo}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Comprado:\t{self.comprado}{bcolors.ENDC}")