"""
Calcular el Precio de Venta

Enunciado: Dado el valor de venta de un producto, se debe calcular el 
Impuesto General a las Ventas(IGV), que es del 18%, y a partir de eso,
determinar el precio de venta final.

Mejora: En esta practica, vamos a crear un programa en Python que permita 
al usuario ingresar el valor de venta del producto. Luego, el sistema 
realizará los calculos necesarios para hallar el IGV y el precio de venta 
final
"""
IGV = 0.18
price = float(input("Introduzca el precio: "))

igv = IGV * price
total_price = igv + price

print(f"Total Price: {total_price:.2f}")
