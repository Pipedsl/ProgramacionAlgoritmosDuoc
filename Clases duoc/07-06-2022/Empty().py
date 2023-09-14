#Retorna un arreglo de las dimensiones especificadas pero con datos no inicializados.
import numpy as np
arreglo_vacio = np.empty([3,3])
for i in range(3):
    for j in range (3):
        print(arreglo_vacio[i][j])
        
#tipo str

arreglo_vacio = np.empty([3,3], )
for i in range(3):
    for j in range (3):
        print(arreglo_vacio[i][j])


