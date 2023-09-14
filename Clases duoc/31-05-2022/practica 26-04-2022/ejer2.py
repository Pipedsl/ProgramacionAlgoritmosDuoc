puntuacion=float(input("\nIngrese su puntuación: "))
if puntuacion==0.0:
    nivel="Inaceptable"
    print(f"\n\tSu puntuación es inaceptable\n\n\tBonificación: $0")
elif puntuacion==0.4:
    nivel="Aceptable"
    bonificacion=puntuacion*2400000
    print(f"\n\tSu puntuación es: {puntuacion}, su nivel es: {nivel}\n\n\tBonificación: ${bonificacion}")
elif puntuacion==0.6:
    nivel="Meritorio"
    bonificacion=puntuacion*2400000
    print(f"\n\tSu puntuación es: {puntuacion}, su nivel es: {nivel}\n\n\tBonificación: ${bonificacion}")
else:
    print("XXXXXXXX  ERROR AL DIGITAR SU PUNTUACIÓN  XXXXXXXX")