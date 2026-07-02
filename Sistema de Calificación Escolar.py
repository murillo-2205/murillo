def clasificar_nota(nota):
    if nota < 60:
        return "Reprobado"
    elif nota <= 89:
        return "Aprobado"
    else:
        return "Excelente"

nota = float(input("Ingrese la nota final del alumno: "))

resultado = clasificar_nota(nota)

print("Calificación:", resultado)