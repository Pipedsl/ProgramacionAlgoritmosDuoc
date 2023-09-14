#Contador se utiliza para contar cuando ocurre un suceso
#en este caso cuantos numeros pares se ingresaron
cont=0;
num1=int(input("ingrese primer numero: "))
if num1 % 2==0:
    cont=cont+1
num2=int(input("ingrese primer numero: "))
if num2 % 2==0:
    cont=cont+1
num3=int(input("ingrese primer numero: "))
if num3 % 2==0:
    cont=cont+1
print(cont)