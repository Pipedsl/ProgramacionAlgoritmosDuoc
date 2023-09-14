import numpy as np
#Forma 1

matriz = np.array([[2,1,3],[6,2,9]]) #Filas 2 x columnas 3 
# F0 1 2
#C
#0 2 1 3
#1 6 2 9

#Forma 2

matriz2 = np.array([
[2,1,3],  #Vector1
[6,2,9]   #Vector2 
])

#Imprimir Matriz
print(matriz[0][0]) #Resultado es 2

#Recorrer la matriz con doble for

for i in range (2):
    for j in range (3):
        print(matriz[i][j])  # recorre fila y columna = como resultado obtendremos todos los valores de la matriz recorridos