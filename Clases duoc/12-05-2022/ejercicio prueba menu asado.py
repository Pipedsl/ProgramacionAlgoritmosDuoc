#intento evaluación 
asado_de_costilla = 7490
parrillada_Thor = 9990
milanesa = 5990
entrecot = 8690

print("Bienvenido a Parrillada de Thor escoja su opción: \n\t1) Asado de Costilla \n\t2) Parrillada Thor \n\t3) Milanesa \n\t4) Entrecot \n\t5) Salir")
op = int(input("Seleccione una opción: "))
if op == 1:
    op1 = asado_de_costilla
    print(f"Usted escogio Asado de costilla: ${op1} pesos")
    ct1 = int(input("Seleccione la cantidad de platos: "))
    top1= op1*ct1
elif op == 2:
    op2 = parrillada_Thor
    print(f"Usted escogio Parrillada Thor: ${op2} pesos")
    ct2 = int(input("Seleccione la cantidad de platos: "))
    top1= op2*ct2
elif op == 3:
    op3 = milanesa
    print(f"Usted escogio Milanesa: ${op3} pesos")
    ct3 = int(input("Seleccione la cantidad de platos: "))
    top1= op3*ct3
elif op == 4:
    op4 = entrecot
    print(f"Usted escogio entrecot: ${op4} pesos")
    ct4 = int(input("Seleccione la cantidad de platos: "))
    top1= op4*ct4
print(f"El total de su pedido es: ${top1} pesos")




        
