def convertir_usd_a_eur(cantidad_usd, tasa_cambio):
    euros = cantidad_usd * tasa_cambio
    return euros

cantidad_usd = float(input("Ingrese la cantidad en dólares (USD): "))
tasa_cambio = float(input("Ingrese la tasa de cambio (1 USD a EUR): "))

resultado = convertir_usd_a_eur(cantidad_usd, tasa_cambio)

print("La cantidad en euros es:", resultado, "EUR")