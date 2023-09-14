#Indice 0=posición 1, 1= posición 2, 2= posición 3, 3 4 ...
from unittest.util import strclass


lista=[12,"Python",3.1416]
print(lista[0]) #12
print(lista[1]) #Python
print(lista[2]) #3.1416
print(lista[-1])#Ultimo elemento de la lista(Para acceder rapido a los ultimos elementos)
print(lista[-3])#Penultimo elemento de la lista
lista.append(3) #Para agregar elementos al final de la lista creada
print(lista)#imprime toda la lista en consola
lista.append(input("Ingrese un valor a la lista: ")) #append con input valor en string
print(lista)
lista.extend([25,"hola"]) #Permite añadir una lista a la inicial, tambien puedes agregar una variable que contenga listas
print(lista)#imprime todo lo visto anterior
lista.insert(2,"buenas") #Permite añadir un elemento en una posición determinada (primer numero corresponde dónde ira insertado 2=posición 3 de la lista recordar que parte de 0 como posición 1) (no elimina el que estaba en esa posición solo lo mueve)
print(lista)
lista.remove(12)#Elimina un objeto de la lista, en este casó el 12
print(lista)
lista.pop()#al estar vacio elimina el ultimo elemento de la lista
lista.pop(1)#Elimina el elemento que este en el indice 1(segunda posición, recordando que indice 0 es la primera poscición)
print(lista)
lista.reverse()#Permite invertir el orden de la lista
print(lista)
#lista.sort()   #Permite ordenar los elementos de menor a mayor (pero solo con números, no acepta string, si hay string hay error)
print(lista)
#lista.sort(reverse=True)#sort tambien permite ordenar los elementos de mayor a menor debe ir reverse=True