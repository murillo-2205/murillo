nota = int(input("Ingrese una nota del 1 al 5: "))

match nota:
    case 1 | 2:
        print("Insuficiente")
    case 3:
        print("Suficiente")
    case 4:
        print("Notable")
    case 5:
        print("Sobresaliente")
    case _:
        print("Nota no válida")