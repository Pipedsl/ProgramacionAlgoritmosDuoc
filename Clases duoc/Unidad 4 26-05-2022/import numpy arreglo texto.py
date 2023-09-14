import numpy as np

v_arreglo = np.array(["Pedro",5,7])

v_arreglo[1] = input("Ingrese un nombre .-")

for i in range (len(v_arreglo)):
    print(f"Valor {i+1} del arreglo es : {v_arreglo [i]}")


