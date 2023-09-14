#Ejercicio programa promedio
Xdalg=float(input("Ingrese su nota final de Diseño de Algoritmos:  \n\t"))
Xlab=float(input("Ingrese su nota final de Laboratorio:  \n\t"))
Xfinal=(Xdalg+Xlab)/2
print("El promedio final es:\n\t",Xfinal)
if Xfinal>=6:
    print("Buen resultado de aprendizaje")
elif Xfinal>=4 and Xfinal<6:
    print("El resultado de aprendizaje puede ser mejor")
else:
    print("El resultado de aprendizaje no es lo esperado")