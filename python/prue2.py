age=int(input("Ingrese su edad: "))
print("\tChild: 0 to 11\n\tTeen: 12 to 17 \n\tAdult: 18 to 64")
if age <= 11:
    print("Child")
elif age ==17 or age < 17 and age>11:
    print("Teen")
else:
    print("Adult")