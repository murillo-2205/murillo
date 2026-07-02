def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

resultado = calcular_area_triangulo(base, altura)

print("El área del triángulo es:", resultado)