import random as rd

#crear arreglos y asignarles valores aleatorios

Arreglo = [0]*100
count = 1

for i in range(len(Arreglo)):
    Arreglo[i] = rd.randrange(10)
    print (f"{count}) {Arreglo[i]}")
    count = count+1


