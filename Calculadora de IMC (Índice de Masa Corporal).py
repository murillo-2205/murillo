def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)

    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Sobrepeso"

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

resultado = calcular_imc(peso, estatura)

print("Clasificación:", resultado)