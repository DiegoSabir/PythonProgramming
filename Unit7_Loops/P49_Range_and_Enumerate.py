for n in range(5):
    print(n)

for n in range(10, 20):
    print(n)

for n in range(10, 20, 2):
    print(n)

fruits = ["Pera", "Uva", "Manzana"]
for indice, valor in enumerate(fruits):
    print(indice, valor)

for indice, valor in enumerate(fruits, start = 1):
    print(indice, valor)