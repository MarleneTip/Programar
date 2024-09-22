def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el descuento aplicado a un monto total.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10%).
    :return: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
monto1 = 1500  # Ejemplo de monto total de la compra
descuento1 = calcular_descuento(monto1)  # Llamada con porcentaje por defecto
print(f"Descuento (10% de {monto1}): {descuento1}")

monto2 = 800  # Otro ejemplo de monto total de la compra
porcentaje2 = 15  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, porcentaje2)  # Llamada con porcentaje personalizado
print(f"Descuento (15% de {monto2}): {descuento2}")