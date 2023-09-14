Beatles = [] #OK
print("Paso 1:", Beatles)
Beatles.append("John Lennon") #OK
Beatles.append("Paul McCartney") #OK
Beatles.append("George Harrison") #OK
print("Paso 2:", Beatles)
for i in Beatles:
    Beatles.append(input("Agregue a Stu Sutcliffe: "))
    Beatles.append(input("Agregue a Pete Best: "))
    if Beatles[4] == "Pete Best":
        break
print("Paso 3:", Beatles)
del Beatles[-1] #OK
del Beatles[-1] #OK
print("Paso 4:", Beatles)
Beatles.insert(0,"Ringo Star") #OK
print("Paso 5:", Beatles)



print("Los Fav", len(Beatles))