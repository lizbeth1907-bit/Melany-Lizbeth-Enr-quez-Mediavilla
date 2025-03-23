# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamadas a la función con diferentes valores
monto_1 = 150
descuento_1, monto_final_1 = calcular_descuento(monto_1)

monto_2 = 300
porcentaje_descuento_2 = 20
descuento_2, monto_final_2 = calcular_descuento(monto_2, porcentaje_descuento_2)

# Mostrar resultados
print(f"Compra 1 - Monto: ${monto_1}, Descuento: ${descuento_1}, Monto final: ${monto_final_1}")
print(f"Compra 2 - Monto: ${monto_2}, Descuento ({porcentaje_descuento_2}%): ${descuento_2}, Monto final: ${monto_final_2}")