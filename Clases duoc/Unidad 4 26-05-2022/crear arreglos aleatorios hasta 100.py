import random as rd


Arreglo = [0]*100
count = 1

for i in range(len(Arreglo)):
    Arreglo[i] = rd.randrange(10) #100 numeros random
    print(f"{count}) {Arreglo[i]}")

    count += 1




