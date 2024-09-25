counter = 1
while counter <= 10:
    print(counter)
    counter += 1

########################################################################################

product_list = []
product = ""

# Bucle para agregar productos
while product.lower() != "finish":
    product = input("Ingresa un producto (o escribe 'finish' para terminar): ")
    if product.lower() != "finish":  # Evita agregar 'finish' a la lista
        product_list.append(product)

# Mostrar la lista de productos
print("Lista de productos")
contador = 1
indice = 0

# Bucle para mostrar la lista con índices
while indice < len(product_list):
    print(f"{contador}. {product_list[indice]}")
    indice += 1
    contador += 1
