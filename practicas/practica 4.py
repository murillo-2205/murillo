#operador matematico de murillo: crea un programa donde determine cual es el valor de erick, usando if elif else
#si el valor de erick es entero positivo entonces es valido si es negativo es invalido.

def erick(murillo):
    if murillo <0:
        return 'invalido'
    elif murillo <=100:
        return 'es valido'
    else:
        return 'valor fuera de rango'

murillo= int(input('ingrese un valor'))
final= erick(murillo)
print('tu valor', final)



