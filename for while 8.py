#Escribe un programa que imprima la serie de Fibonacci hasta el enésimo término,
#donde el valor de n lo ingresa el usuario, utilizando un bucle for.

numero = int(input("Ingrese la cantidad de términos: "))

tio = 0
murillo = 1

for i in range(numero):
    print(tio)
    branyu = tio + murillo
    tio = murillo
    murillo = branyu