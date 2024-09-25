dictionary1 = {"nombre":"Juan", "edad":30 , "ciudad":"Madrid"}

#
for valor in dictionary1:
    print(valor)

#
for valor in dictionary1:
    print(dictionary1[valor])

#
for valor in dictionary1.values():
    print(valor)

#
for clave, valor in dictionary1.items():
    print(clave, valor)