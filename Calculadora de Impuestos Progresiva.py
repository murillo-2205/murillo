def calcular_salario_neto(salario_bruto):
    if salario_bruto < 1500:
        impuesto = 0
    elif salario_bruto <= 3000:
        impuesto = (salario_bruto - 1500) * 0.10
    else:
        impuesto = (salario_bruto - 3000) * 0.20

    salario_neto = salario_bruto - impuesto
    return salario_neto

salario = float(input("Ingrese el salario bruto mensual: $"))

resultado = calcular_salario_neto(salario)

print("El salario neto es: $", resultado)