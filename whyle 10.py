#Escribe un programa que pida al usuario  ingresar una
#contraseña y repita la solicitud mientras la contraseña ingresada 
#sea incorrecta. El programa debe continuar hasta que el
#usuario ingrese la contraseña correcta. Utiliza
#una estructura whilepara simular un do while.

contraseña_correcta = "yosoytutio"

contraseña = ""

while contraseña != contraseña_correcta:
    contraseña = input("Ingrese la contraseña: ")

print("¡Contraseña correcta! Acceso permitido tio.")