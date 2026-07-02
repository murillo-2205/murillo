def determinar_primo(numero):
    match numero:
        case 2 | 3 | 5 | 7:
            return "Número primo"
        case 1 | 4 | 6 | 8 | 9 | 10:
            return "Número compuesto"
        case _:
            return "Número fuera del rango"

numero = int(input("Ingrese un número del 1 al 10: "))

resultado = determinar_primo(numero)

print(resultado)