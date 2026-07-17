#Sistema de Calificación Escolar: Crea una función que reciba la nota final de un
#alumno. Dentro de la función, usa if-elif-else para clasificarla: menos de 70 es
#"Reprobado", entre 70 y 89 es "Aprobado" y 90 o más es "Excelente". Retorna este
#tring e imprímelo.

def calificacion(hola):
    if hola <70:
        return 'reprobado'
    elif hola <89:
        return 'aprobado'
    else:
        return 'excelente'
hola= float(input('ingrese la calificacion final'))

resultado= calificacion(hola)

print('tu calificacion', resultado)



