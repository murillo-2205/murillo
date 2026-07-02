def saludar_usuario(nombre, hora_dia):
    if hora_dia == "mañana":
        return f"¡Buenos días, {nombre}!"
    elif hora_dia == "tarde":
        return f"¡Buenas tardes, {nombre}!"
    elif hora_dia == "noche":
        return f"¡Buenas noches, {nombre}!"
    else:
        return f"Hola, {nombre}."

nombre = input("Ingrese su nombre: ")
hora_dia = input("Ingrese la hora del día (mañana, tarde o noche): ").lower()

print(saludar_usuario(nombre, hora_dia))