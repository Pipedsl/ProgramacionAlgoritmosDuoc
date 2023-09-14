#Zeros: devuelve un array de las dimensiones indicadas, pero cada uno de sus componentes se inicializa con valor cero (0), de tipo float (0.0)
import numpy as np

arreglos_ceros = np.zeros([2,3])
for i in range (2):
    for j in range (3):
        print(arreglos_ceros[i][j]) # el resultado anterior se rellena con 0.0

#podemos especificar el tipo de valor sea entero usando el siguiente codigo
arreglos_ceros = np.zeros([2,3] , type (int))
for i in range (2):
    for j in range (3):
        print(arreglos_ceros[i][j])
        


