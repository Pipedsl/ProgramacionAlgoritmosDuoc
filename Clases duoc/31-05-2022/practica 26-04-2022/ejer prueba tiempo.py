mascarilla_quirurgica=1500
mascarilla_quimica=1000
mascarilla_filtro_simple=2000
mascarilla_doble_filtro=3000
compra=int(input("Ingrese el número de modelo de mascarilla que desea comprar:\n\t 1- Mascarilla Quirúrgica = $1.500\n\t 2- Mascarilla Química = $1.000\n\t 3- Mascarilla Filtro Simple = $2.000\n\t 4- Mascarilla Doble Filtro = $3.000 \n\tAquí -->"))
cantidad=int(input("Ingrese la cantidad de mascarillas que desea: "))
codigo_descuento=input("Ingrese el codigo de descuento: ")
if compra==1:
    total=mascarilla_quirurgica*cantidad
    if codigo_descuento=="TEMPO10":
        codigo_valido=total*0.9
        print(f"Tiene un 10% de descuento en su compra, El total de su compra es: ${codigo_valido}")
    else:
        print(f"No tiene descuento, El total de su compra es: ${total}")
elif compra==2:
    total=mascarilla_quimica*cantidad
    if codigo_descuento=="TEMPO10":
        codigo_valido=total*0.9
        print(f"Tiene un 10% de descuento en su compra, El total de su compra es: ${codigo_valido}")
    else:
        print(f"No tiene descuento, El total de su compra es: ${total}")
elif compra==3:
    total=mascarilla_filtro_simple*cantidad
    if codigo_descuento=="TEMPO10":
        codigo_valido=total*0.9
        print(f"Tiene un 10% de descuento en su compra, El total de su compra es: ${codigo_valido}")
    else:
        print(f"No tiene descuento, El total de su compra es: ${total}")
else:
    total=mascarilla_doble_filtro*cantidad
    if codigo_descuento=="TEMPO10":
        codigo_valido=total*0.9
        print(f"Tiene un 10% de descuento en su compra, El total de su compra es: ${codigo_valido}")
    else:
        print(f"No tiene descuento, El total de su compra es: ${total}")
