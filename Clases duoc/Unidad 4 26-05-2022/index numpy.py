import numpy 

a= numpy.array([1,2,3,4,5])

index = numpy.where(a==5) #encontrar el indice de un valor

print("5 se encuentra en el indice: ", index[0]) #[0] para que python recorra desde el 0 los indices 