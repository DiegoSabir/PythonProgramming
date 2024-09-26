def saludar():
    print("Hola Mundo")
print(saludar())


def saludar_v2(nombre):
    print(f"Holaa, {nombre}")
print(saludar_v2("Diego"))


def saludar_v3(nombre):
    return f"Hola, {nombre}"
print(saludar_v3("Diego"))

saludo = saludar_v3("Diego")
print(saludo)

def suma(a, b):
    return a + b
print(suma(40, 50))