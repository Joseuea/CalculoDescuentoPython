def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento y devuelve el monto descontado."""
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamadas a la función
monto1 = 100
descuento1, total1 = calcular_descuento(monto1)

monto2 = 200
descuento2, total2 = calcular_descuento(monto2, 15)

# Resultados
print(f"Monto: ${monto1}, Descuento: ${descuento1}, Total a pagar: ${total1}")
print(f"Monto: ${monto2}, Descuento: ${descuento2}, Total a pagar: ${total2}")
