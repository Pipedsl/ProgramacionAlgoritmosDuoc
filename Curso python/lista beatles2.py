Beatles = [] #OK
print("Paso 1:", Beatles)
Beatles.append("John Lennon") #OK
Beatles.append("Paul McCartney") #OK
Beatles.append("George Harrison") #OK
print("Paso 2:", Beatles)
for members in range (2):
    Beatles.append(input("Nuevo miembro de la banda: "))
print("Paso 3:", Beatles)
del Beatles[-1] #OK
del Beatles[-1] #OK
print("Paso 4:", Beatles)
Beatles.insert(0,"Ringo Star") #OK
print("Paso 5:", Beatles)



print("Los Fav", len(Beatles))