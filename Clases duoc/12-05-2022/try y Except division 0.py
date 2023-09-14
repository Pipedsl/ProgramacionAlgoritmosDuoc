# try y Except
#try = intentar/tratar
#except = se ejecuta otra instrucción, usado para no detener el programa en un error
#Ejemplo 1
a=5
b=0
try:
    c=a/b
    print(f"El resultado es: {c}")
except ZeroDivisionError:
    print("No se ha podido realizar la división")

