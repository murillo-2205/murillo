jugador1 = input("Jugador 1 (Piedra, Papel o Tijera): ")
jugador2 = input("Jugador 2 (Piedra, Papel o Tijera): ")

if jugador1 == jugador2:
    print("Empate")
else:
    if jugador1 == "Piedra":
        if jugador2 == "Tijera":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")
    elif jugador1 == "Papel":
        if jugador2 == "Piedra":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")
    elif jugador1 == "Tijera":
        if jugador2 == "Papel":
            print("Gana el Jugador 1")
        else:
            print("Gana el Jugador 2")
    else:
        print("Opción no válida")