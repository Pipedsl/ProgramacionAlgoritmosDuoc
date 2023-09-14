#Calculadora
o=input("\nIngrese la letra de la operación que desee realizar \n\ts. para Suma\n\tr. para Resta \n\tp,m. para Multiplicación\n\td. para División \n\t\t-->").lower ()
n1=float(input("Ingrese el primer número: \n\t -->"))
n2=float(input("Ingrese el segundo número: \n\t-->"))
if o=="s":
    suma=n1+n2
    print("El resultado de",n1,"+",n2,"es:\n\t=",suma)
elif o=="r":
    resta=n1-n2
    print("El resultado de",n1,"-",n2,"es:\n\t=",resta)
elif o=="p" or o=="m":
    multi=n1*n2
    print("El resultado de",n1,"*",n2,"es:\n\t=",multi)
else:
    divi=n1/n2
    print("El resultado de",n1,"/",n2,"es:\n\t=",divi)