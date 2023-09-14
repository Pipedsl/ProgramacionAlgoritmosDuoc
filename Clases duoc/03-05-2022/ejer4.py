#factorial
fact = 1
i = 1
num = int(input("Ingrese un número: "))
while i <= num:
    fact = fact * i
    i = i + 1
print(f"El factorial de {num} es : {fact}")
