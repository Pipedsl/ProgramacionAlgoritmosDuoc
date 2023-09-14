#Menú con while, try if y except
sw = 1
while sw == 1:
    print("\t1. Opción 1")
    print("\t2. Opción 2")
    print("\t3. Opción 3")
    op = int(input("\n\tSeleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print("ha seleccionado la opción 1")
                continu = int(input("Desea salir \n\t1=Si \n\t2=No \n\t"))
                if continu == 1:
                    print("Adios")
                    sw = 0
            if op == 2:
                print ("Ha seleccionado la opción 2")
                continu = int(input("Desea salir \n\t1=Si \n\t2=No \n\t"))
                if continu == 1:
                    print("Adios")
            if op == 3:
                print("Usted desea salir del menú")
                sw = 0
    except:
        print("Ingreso erroneo ")
