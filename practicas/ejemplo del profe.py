#Inventario de productos

#Una tienda guarda sus productos en una lista de tuplas con el formato (nombre, precio). Escribe un programa que calcule el precio promedio de todos los productos. 
#El producto de mayor precio
#El producto de menor precio
#La suma del inventario

def obtener_mayor(tupla):
    return tupla[1]

productos = [
    ("Arroz Selecto 5 lb", 385.00),
    ("Habichuelas Rojas Linda 2 lb", 145.00),
    ("Aceite Crisol 32 oz", 310.00),
    ("Azúcar Crema 2 lb", 95.00),
    ("Sal Marina 1 lb", 35.00),
    ("Leche Rica 1 litro", 92.00),
    ("Queso de Hoja", 185.00),
    ("Salami Induveca 1 lb", 165.00),
    ("Jamón Cocido Induveca", 145.00),
    ("Huevos (cartón de 30)", 295.00),
    ("Pan Sobao", 85.00),
    ("Café Santo Domingo 1 lb", 345.00),
    ("Chocolate Embajador", 275.00),
    ("Avena Quaker", 120.00),
    ("Pasta Milano Espaguetis", 58.00),
    ("Salsa Victorina", 78.00),
    ("Mayonesa Baldom", 135.00),
    ("Ketchup Baldom", 95.00),
    ("Vinagre Linda", 65.00),
    ("Sazón Completo Baldom", 55.00),
    ("Sardinas Paco Fish", 85.00),
    ("Atún Paco Fish", 125.00),
    ("Galletas Export Soda", 72.00),
    ("Galletas Dino", 65.00),
    ("Jugo Frutop", 42.00),
    ("Refresco Kola Real 2 L", 95.00),
    ("Agua Planeta Azul 1.5 L", 40.00),
    ("Yuca 1 lb", 35.00),
    ("Plátanos Verdes (unidad)", 28.00),
    ("Guineos (unidad)", 12.00),
    ("Papa 1 lb", 45.00),
    ("Cebolla Roja 1 lb", 55.00),
    ("Ajo (cabeza)", 30.00),
    ("Tomate 1 lb", 58.00),
    ("Ají Cubanela 1 lb", 65.00),
    ("Pollo Fresco 1 lb", 98.00),
    ("Carne de Res 1 lb", 245.00),
    ("Chuleta Ahumada 1 lb", 215.00),
    ("Detergente Ace 500 g", 115.00),
    ("Jabón Bolívar", 48.00),
    ("Suavizante Suavitel", 185.00),
    ("Cloro Brillante", 75.00),
    ("Papel Higiénico Scott (4 rollos)", 175.00),
    ("Pasta Dental Colgate", 95.00),
    ("Cepillo Dental Oral-B", 75.00),
    ("Shampoo Sedal", 210.00),
    ("Desodorante Rexona", 165.00),
    ("Jabón de Baño Protex", 65.00),
    ("Velas La Milagrosa", 90.00),
    ("Fósforos Tres Estrellas", 25.00)
]

precio_total = sum(precio for _, precio in productos)
cantidad_productos = len(productos)
precio_promedio = precio_total / cantidad_productos if  cantidad_productos > 0 else 0
# producto_mayor_precio = max(productos, key=lambda x: x[1])
# producto_menor_precio = min(productos, key=lambda x: x[1])  

producto_mayor_precio = max(productos, key=obtener_mayor)
producto_menor_precio = min(productos, key=obtener_mayor)

print(f"Precio promedio de los productos: {precio_promedio:.2f}")
print(f"cantidad de productos: {cantidad_productos}")
print(f"Producto de mayor precio: {producto_mayor_precio[0]} - Precio: {producto_mayor_precio[1]:.2f}")
print(f"Producto de menor precio: {producto_menor_precio[0]} - Precio: {producto_menor_precio[1]:.2f}")
print(f"Suma del inventario: {precio_total:.2f}")