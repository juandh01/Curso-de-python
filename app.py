import random

opciones = ["rock", "paper", "scissors"]
puntos = 0
rondas = 0

print("👊 Bienvenido al juego de Piedra, Papel o Tijera (contra la compu)")

while True:
    jugador = input("\nElige rock, paper o scissors: ").lower()
    if jugador not in opciones:
        print("⚠️ Opción inválida. Por favor elige rock, paper o scissors.")
        continue

    compu = random.choice(opciones)
    print(f"🖥️ La compu eligió: {compu}")

    if jugador == compu:
        print("😐 ¡Empate!")
    elif (
        (jugador == "rock" and compu == "scissors") or
        (jugador == "scissors" and compu == "paper") or
        (jugador == "paper" and compu == "rock")
    ):
        print("🏆 ¡Ganaste!")
        puntos += 1
    else:
        print("💀 Perdiste.")

    rondas += 1
    jugar_de_nuevo = input("¿Quieres jugar otra ronda? (s/n): ").lower()
    if jugar_de_nuevo != "s":
        break

print("\n🎯 Fin del juego")
print(f"Jugaste {rondas} rondas y ganaste {puntos}. ¡Gracias por jugar!")

