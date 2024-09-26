a = 10
b = 5

print(globals())  # Imprime las variables globales

def suma(n1, n2):
    n = n1 + n2
    print(locals())  # Imprime las variables locales
    return n  # Devuelve la suma

print(suma(a, b))  # Ahora imprime la suma después de imprimir las locales

def func1():
    print(a)

# Comentario: no se puede modificar el valor de una variable global desde dentro de una función sin "global"
"""
def func1():
    a += 1
"""

def func2():
    global a
    a += 1

func2()  # Modifica el valor de la variable global
print(a)  # Imprime el valor actualizado de la variable global

def func3():
    c = 0
    def func4():
        nonlocal c
        c += 1
    func4()  # Modifica 'c'
    print(c)  # Imprime el valor de 'c'

print(func3())  # Llama a func3(), que imprimirá el valor de 'c'
