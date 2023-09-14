billete = float(input("Ingrese el precio de los productos seleccionados: $")) #CLP
porcentaje_propina = 0.1 #10%
porcentaje_impuestos = 0.067 #6.7%

propina = billete * porcentaje_propina
print(f"propina: {propina}")

impuestos = billete * porcentaje_impuestos
print(f"impuestos: {impuestos}")

total = billete + impuestos + propina
print(f"Total: {total}")

