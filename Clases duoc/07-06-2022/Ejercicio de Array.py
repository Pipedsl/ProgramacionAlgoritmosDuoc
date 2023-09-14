import numpy as np

cabanas = np.array(["D","D","D","D","D","D","D","D","D","D"])

for i in range (10):
    print(cabanas[i])
sel_c = int(input("Seleccione el número de cabaña que desea Reservar: "))
if cabanas[sel_c] == "D":
        cabanas[sel_c] = "R"
print("Cabaña reservada n°: ", sel_c)
print("Desea realizar alguna modificación: \n1) Si\n2) No ")
mod = input("-->")
if mod == 1:
    cabanas[sel_c] = "D"
sel_c = int(input("Seleccione el número de cabaña que desea Reservar: "))
if cabanas[sel_c] == "D":
        cabanas[sel_c] = "R"
print("Cabaña reservada n°: ", sel_c)
print(cabanas)