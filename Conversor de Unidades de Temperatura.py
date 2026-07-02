temperatura = float(input("Ingrese la temperatura en Celsius: "))
escala = input("Ingrese la escala de destino (C, F, K): ").upper()

match escala:
    case "C":
        print("Temperatura:", temperatura, "°C")
    case "F":
        fahrenheit = (temperatura * 9 / 5) + 32
        print("Temperatura:", fahrenheit, "°F")
    case "K":
        kelvin = temperatura + 273.15
        print("Temperatura:", kelvin, "K")
    case _:
        print("Escala no válida.")