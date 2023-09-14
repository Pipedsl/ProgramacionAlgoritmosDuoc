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

class Persona:

    def __init__(self, rut, nombre, apellido, dpto):
        try:
            if correctAttr(rut, int, attrname='Rut', objname="Persona"):
                self.rut = rut
            else:
                raise AttributeError
            if correctAttr(nombre, str, attrname='nombre', objname="Persona"):
                self.nombre = nombre
            else:
                raise AttributeError
            if correctAttr(apellido, str, attrname='apellido', objname="Persona"):
                self.apellido = apellido
            else:
                raise AttributeError
            if correctAttr(dpto, str, attrname='dpto', objname="Persona"):
                self.dpto = dpto
            else:
                raise AttributeError
            print(f"{bcolors().OKGREEN}[✓]{bcolors().ENDC} {bcolors().OKCYAN}{bcolors().HEADER}[Persona] {bcolors().OKCYAN}Creada correctamente {bcolors().HEADER}[Persona]{bcolors().ENDC} {bcolors().OKGREEN}[✓]{bcolors().ENDC}")
        except AttributeError as er:
            print(f"{bcolors().FAIL}[✘]{bcolors().HEADER}[Persona]{bcolors().ENDC} {bcolors().FAIL}No se pudo inicializar persona. Comprueba que los datos estén correctamente ingresados{bcolors().FAIL} {bcolors().HEADER}[Persona]{bcolors().FAIL}[✘]{bcolors().ENDC}")

    def contructor(self):
        self.rut = 0 
        self.nombre = ""
        self.apellido = ""
        self.dpto = ""

    def imprimirPersona(self):    
        print(f"{bcolors.HEADER}\n --- Informacion de {self.nombre} --- \n")
        print(f"{bcolors.OKGREEN}Rut:\t{self.rut}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Nombre:\t{self.nombre}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Apellido:\t{self.apellido}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}Dpto:\t{self.dpto}{bcolors.ENDC}")
        