year = int(input("Introduce un año:"))

if year > 1582:
    if year % 4:
        year = "Año Común"
    elif year % 100:
        year = "Año Bisiesto"
    elif year % 400:
        year = "Año Común"
    else:
        year = "Año Bisiesto"
else:
    print("No dentro del período del calendario Gregoriano")

print("El tipo de año es: ",year)
