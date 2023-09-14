print("Los siguiente son los partidos disponibles para su votación: \n\tA) Partido rojo \n\tB) Partido verde \n\tC) Partido azul\n\t")
voto=input("Ingrese su voto: ")
if voto.upper() == "A":
    print("\nUsted voto A por el Partido Rojo")
elif voto.upper() == "B":
    print("\nUsted voto B por el Partido Verde")
elif voto.upper() == "C":
    print("\nUsted voto C por el Partido Azul")
else:
    print("Su voto no es valido")