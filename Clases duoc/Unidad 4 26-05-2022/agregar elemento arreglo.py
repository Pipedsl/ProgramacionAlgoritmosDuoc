import numpy 

a= numpy.array([1,2,3,4,5])

index = numpy.where(a==5)

print("5 se encuentra en el indice: ", index[0])