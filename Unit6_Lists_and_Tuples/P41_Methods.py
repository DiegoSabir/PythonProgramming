fruits = ["manzana", "naranja", "platano"]
print(fruits)

# Agregamos "uva" al final
fruits.append("uva")
print(fruits)

# Extendemos la lista con ["pera", "fresa"]
new_fruits = ["pera", "fresa"]
fruits.extend(new_fruits)
print(fruits)

# Insertamos "mango" al principio de la lista
fruits.insert(0, "mango")
print(fruits)

# Eliminamos "platano"
fruits.remove("platano")
print(fruits)

# Eliminamos el último elemento de la lista con pop()
fruits.pop()
print(fruits)

# Mostramos el índice de "uva"
index_uva = fruits.index("uva")
print(index_uva)

# Contamos cuántas veces aparece "uva"
count_uva = fruits.count("uva")
print(count_uva)

# Invertimos la lista
fruits.reverse()
print(fruits)
