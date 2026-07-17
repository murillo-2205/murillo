#Escribe un programa que pida al usuario un número entero positivo.
#El programa debe contar cuántos dígitos tiene el número utilizando un bucle while.

tio= int(input('ingrese un numero entero positivo'))


contadora = 0

while tio > 0:
    tio = tio // 10
    contadora += 1

print("El número tiene", contadora, "dígitos.")