#except try, while y break
#while bucle seguir intentando
#break= terminar el programa si se cumple
while True:
    try:
        x=int(input("Introduce un número: "))
        break
    except ValueError:
        print("¡ERROR! No es un número. prueba de nuevo...")