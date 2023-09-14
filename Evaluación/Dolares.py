dolar = float(input("Ingrese el precio del dolar en pesos chilenos: $"))
UF = float(input("Ingrese el precio de la UF en pesos chilenos: $"))
UTM = float(input("Ingrese el precio de la UTM en pesos chilenos: $"))

print("Que desea convertir a Peso chileno (CLP): \n\t1) Dolar \n\t2) UF \n\t3) UTM ")
cambio = int(input("Ingrese el número: "))

if cambio == 1:
    print("Usted eligio Dolar")
    cantidad = float(input("Ingrese la cantidad que desea convertir a CLP: "))
    total = dolar*cantidad
    print(f"El valor del dolar es: {dolar} el cambio de {cantidad} dolares a CLP es: {total}")
elif cambio == 2:
    print("Usted eligio UF")
    cantidad = float(input("Ingrese la cantidad que desea convertir a CLP: "))
    total = UF*cantidad
    print(f"El valor de la UF es: {UF} el cambio de {cantidad} UF a CLP es: {total}")
elif cambio == 3:
    print("Usted eligio UTM")
    cantidad = float(input("Ingrese la cantidad que desea convertir a CLP: "))
    total = UTM*cantidad
    print(f"El valor de la UTM es: {UTM} el cambio de {cantidad} UTM a CLP es: {total}")
else:
    print("Valor no admitido")



