list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenación de ambas listas
list = list1 + list2  
print(list)

# Multiplica los elementos de list1 por 3
print(list1 * 3)  

# Asignaciones deben estar separadas de print
list3 = list[0:5]
print(list3)

list4 = list[:3]
print(list4)

list5 = list[3:]
print(list5)

list6 = list[-3:]
print(list6)

list7 = list[-3:-1]
print(list7)

list8 = list[::2]
print(list8)

list9 = list[1::2]
print(list9)

list10 = list[::-1]
print(list10)

# sorted() devuelve una nueva lista ordenada
print(sorted(list10))

# sort() modifica la lista en su lugar, no devuelve nada
list10.sort(reverse=True)
print(list10)
