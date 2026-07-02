def validar_longitud_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

password = input("Ingrese una contraseña: ")

if validar_longitud_password(password):
    print("Contraseña válida.")
else:
    print("Contraseña no válida. Debe tener al menos 8 caracteres.")