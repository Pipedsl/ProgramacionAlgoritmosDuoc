diseño=float(input("Nota Final en Diseño: "))
lab=float(input("Nota final de Laboratorio: ")) 
promedio=(diseño+lab)/2 
print(f"Su promedio es:  {promedio}") 
if promedio >= 6:     
    print("Buen resultado de aprendizaje") 
if promedio >=4 and promedio < 6:
    print("El resultado de aprendizaje puede ser mejor")
if promedio < 4:     
    print("El resultado de aprendizaje no es lo esperado") 



    