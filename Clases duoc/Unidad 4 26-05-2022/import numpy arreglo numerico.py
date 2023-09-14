import numpy #Siempre se debe importar numpy para trabajar con arreglo tipo número

v_arreglo = numpy.array([1,5,7]) # Arreglo

print(v_arreglo[0]) # indice 0  
print(v_arreglo[1]) # indice 1
print(v_arreglo[2]) # indice 2
print("----------Aqui separé el codigo-----------")
for i in range (len(v_arreglo)): #Uso de For para recorrer el Arreglo
    print(v_arreglo[i])
