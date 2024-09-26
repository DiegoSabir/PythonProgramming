"""
Crea un programa en Python que simule un sistema de descuentos en un
restaurante segun el monto de consumo. El programa debe seguir las
siguientes instrucciones:

    - Solicita al usuario que ingrese la cantidad de consumo en el restaurante.
    - Aplica descuentos segun las siguientes reglas:
        + Si la cantidad de consumo es mayor a $50 pero igual o menor a $100, aplica un descuento del 10%.
        + Si la cantidad de consumo es mayor a $100 pero igual o menor a $200, aplica un descuento del 20%.
        + Si la cantidad de consumo es mayor a $200, aplica un descuento del 30%.
        + Si la cantidad de consumo es igual o menor a $50, no aplica ningun descuento.

Muestra al usuario un resumen de la cuenta con el monto de consumo, el descuento aplicado y el monto final con descuento. 
"""

monto = float(input("Introduzca la cantidad"))

if (monto > 50 and monto <= 100):
    discount = 0.1

elif (monto > 100 and monto <= 200):
    discount = 0.2

elif (monto > 200):
    discount = 0.3

else:
    discount = 0

# Calcula el monto del descuento y el total con descuento
monto_descuento = monto * discount
total = monto - monto_descuento

# Muestra el resumen de la cuenta
print("\nResumen de la cuenta:")
print(f"Consumo original: ${monto:.2f}")
print(f"Descuento aplicado: ${monto_descuento:.2f} ({discount * 100:.0f}%)")
print(f"Monto final con descuento: ${total:.2f}")
