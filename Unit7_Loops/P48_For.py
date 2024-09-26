numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

message = "Hola Mundo"
for letter in message:
    print(letter)

############################


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
for product in product_list:
    print(f"{contador}. {product}")
    contador += 1