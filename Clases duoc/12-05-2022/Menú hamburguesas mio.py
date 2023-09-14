#Menú hamburguesas
hg=1
hs = 1000 #Hamburguesa sola
hq = 1500 #Hamburguesa queso
hd = 2500 #Hamburguesa doble
ppf = 1000 #Porción papas fritas
b = 600 #Bebida
c = 400 #café

while hg== 1:
    print("1. Hamburguesa Sola = $1000 pesos")
    print("2. Hamburguesa Queso = $1500 pesos")
    print("3. Hamburguesa Doble = $2500 pesos")
    print("4. Porción Papas Fritas = $1000 pesos")
    print("5. Bebida = $600 pesos")
    print("6. Café = $400 pesos")
    op = int(input("\n\tSeleccione una opción: "))
    try:
        if(op > 0 and op < 100):
            if op == 1:
                print(f"Ha seleccionado Hamburguesa Sola: ${hs} pesos")
                chs=print(int(input("Ingrese cuantas hamburguesas sola desea: ")))
                v1=chs*hs
                continu = int(input("Desea continuar en el menú \n\t1=Si \n\t2=No \n\t"))
                if continu == 2:
                    print(f"El total de su compra es: ${v1} pesos")
                    hg = 0
            if op == 2:
                print(f"Ha seleccionado Hamburguesa Queso: ${hq} pesos")
                chs=print(int(input("Ingrese cuantas hamburguesas sola desea: ")))
                v1=chs*hq
                continu = int(input("Desea continuar en el menú \n\t1=Si \n\t2=No \n\t"))
                if continu == 2:
                    print(f"El total de su compra es: ${v1} pesos")
                    hg = 0
            if op == 3:
                print(f"Ha seleccionado Hamburguesa Doble: ${hd} pesos")
                chs=print(int(input("Ingrese cuantas hamburguesas sola desea: ")))
                v1=chs*hd
                continu = int(input("Desea continuar en el menú \n\t1=Si \n\t2=No \n\t"))
                if continu == 2:
                    print(f"El total de su compra es: ${v1} pesos")
                    hg = 0
    except: 
        print("Ingreso Erroneo")

