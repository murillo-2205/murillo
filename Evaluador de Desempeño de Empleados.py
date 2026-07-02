def evaluar_bono(ventas_mes, asistencia_perfecta):
    if ventas_mes > 50 and asistencia_perfecta:
        return "Bono Premium"
    elif ventas_mes > 50 or asistencia_perfecta:
        return "Bono Estándar"
    else:
        return "No recibe bono"

ventas_mes = int(input("Ingrese la cantidad de ventas del mes: "))
asistencia_perfecta = input("¿Tiene asistencia perfecta? (si/no): ").lower() == "si"

resultado = evaluar_bono(ventas_mes, asistencia_perfecta)

print(resultado)