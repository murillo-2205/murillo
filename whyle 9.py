#Escribe un programa que pida al usuario un número y luego calcule su factorial utilizando un bucle while.
#El factorial de  un número n es el producto de todos los números enteros desde 1 hasta n.

numero = int(input("Ingrese un número: "))

factorial = 1
i = 1

while i <= numero:
    factorial = factorial * i
    i += 1

print("El factorial de", numero, "es:", factorial)