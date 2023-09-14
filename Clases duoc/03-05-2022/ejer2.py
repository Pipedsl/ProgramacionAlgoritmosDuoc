#cantidad de pares
cont=0
num1=int(input("Ingrese el primer numero: "))
if num1 % 2 ==0:
    cont=cont+1
num2=int(input("Ingrese el segundo numero: "))
if num2 % 2 ==0:
    cont = cont+1
num3=int(input("Ingrese el tercer numero: "))
if num3 % 2 ==0:
    cont = cont+1

print("la cantidad de los pares es ",cont)