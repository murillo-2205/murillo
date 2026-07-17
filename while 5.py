#Escribe un programa que pida al usuario un número entero y luego imprima todos
#los números desde ese número hasta el 0 en orden descendente utilizando un bucle while.

tio = int(input("Ingrese un número entero: "))

while tio >= 0:
    print(tio)
    tio -= 1
