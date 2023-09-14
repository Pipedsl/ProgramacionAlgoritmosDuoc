#while negativo
edad=int(input("Introduce tu edad por favor: "))

while edad < 0:
    print("Has introducido una edad negativa. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))
print("Gracias por colaborar. puedes pasar")
print("Edad del aspirante " + str(edad))