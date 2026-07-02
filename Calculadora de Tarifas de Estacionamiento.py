def calcular_tarifa(horas):
    if horas <= 2:
        costo = horas * 2.00
    else:
        costo = (2 * 2.00) + ((horas - 2) * 1.50)

    return costo

horas = float(input("Ingrese la cantidad de horas: "))

resultado = calcular_tarifa(horas)

print("El costo total del estacionamiento es: $", resultado)