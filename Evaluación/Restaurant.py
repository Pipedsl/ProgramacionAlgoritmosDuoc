churrasco = 1500
completo = 1000
vegetariano = 2000
barros_luco = 3000
codigo = "BAJON15"
print("\nBienvenido Donde Juanita")
print("-------------------------")
print("Lista de precios: ")
print("1) Churrasco = $ 1.500")
print("2) Completo = $ 1.000")
print("3) Vegetariano = $2.000")
print("4) Barros Luco = $3.000")
print("-------------------------")
sandwich = int(input("\nSeleccione el número de Sandwich que desea: "))

if sandwich == 1:
    print("\nUsted selecciono Churrasco")
    cantidad = int(input("Ingrese la cantidad que desea: "))
    total = churrasco * cantidad
    print("\nEl total es: ")
    print(f"{cantidad} Churrascos = {total} ")

elif sandwich == 2:
     print("\nUsted selecciono Completo")
     cantidad = int(input("Ingrese la cantidad que desea: "))
     total = completo * cantidad
     print("\nEl total es: ")
     print(f"{cantidad} Completos = {total}")
elif sandwich == 3:
     print("\nUsted selecciono Vegetariano")
     cantidad = int(input("Ingrese la cantidad que desea: "))
     total = vegetariano * cantidad
     print("\nEl total es: ")
     print(f"{cantidad} Vegetarianos = {total}")
elif sandwich == 4:
     print("\nUsted selecciono Barros Luco")
     cantidad = int(input("Ingrese la cantidad que desea: "))
     total = barros_luco * cantidad
     print("\nEl total es: ")
     print(f"{cantidad} Barros Lucos = {total}")
else:
    print("Valor Invalido")

cod = input("Ingrese codigo de descuento:(si no cuenta con uno precione cualquier tecla) ")

if codigo == cod.upper():
    print("Codigo correcto")
    total = total * 0.85
    print(f"El total con el 15% de descuento es: {total}")
else:
    print("Codigo incorrecto")
    print(f"\nEl total de su compra es: {total}")

print("\n---------------------------------")
print("Gracias por comprar Donde Juanita")
print("---------------------------------")