jugador_1 = "Felipe"
jugador_2 = "Danka"
ronda_actual = 1

print("Comienza el juego!")

print(f"Jugador 1: {jugador_1}")
print(f"Jugador 2: {jugador_2}")
print("-------------------------")

print(f"Ronda {ronda_actual}!")
jugador_1_puntuacion = 10
jugador_2_puntuacion = 13
print(f"{jugador_2} gana con {jugador_2_puntuacion} a {jugador_1_puntuacion}")
print("-------------------------")

print(f"Ronda {ronda_actual + 1}!")
jugador_1_puntuacion = 20
jugador_2_puntuacion = 5
print(f"{jugador_1} Derroto {jugador_2} por {jugador_1_puntuacion-jugador_2_puntuacion} puntos")

