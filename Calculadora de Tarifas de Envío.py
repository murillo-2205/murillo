def calcular_envio(peso, zona):
    match zona:
        case "Norte":
            if peso > 0:
                return peso * 5
        case "Sur":
            if peso > 0:
                return peso * 4
        case "Centro":
            if peso > 0:
                return peso * 3
        case _:
            return "Zona no válida"

peso = float(input("Ingrese el peso del paquete (kg): "))
zona = input("Ingrese la zona (Norte, Sur o Centro): ")

resultado = calcular_envio(peso, zona)

print("Costo del envío:", resultado)