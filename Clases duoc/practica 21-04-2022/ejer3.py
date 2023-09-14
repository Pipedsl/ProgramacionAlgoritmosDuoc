#programa numeros
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
if num1>=num2 and num1>=num3:
    print("El mayor es: ",num1) #tambien se puede invocar con funcion (f{})
elif num2>=num1 and num2>=num3:
    print("El mayor es: ",num2)
elif num3>=num1 and num3>=num2:
    print("El mayor es: ",num3)