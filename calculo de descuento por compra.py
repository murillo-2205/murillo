

monto_compra = float(input("Ingrese el monto total de la compra: $"))
if monto_compra > 100:
    descuento = monto_compra * 0.15
    total_pagar = monto_compra - descuento
else:
    total_pagar = monto_compra
      
print("El total a pagar es: $", total_pagar)
   