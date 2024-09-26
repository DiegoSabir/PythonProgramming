import random

def formato_aleatorio()->str:
    formatos = [
        "Hola {}", "Bienvenido",
        "Es genial verte {}",
        "Saludos {}", "Encantado de conocerte"
    ]

    return random.choice(formatos)

def hola(nombre:str)->str:
    if nombre == "":
        return "Error: Nombre vacio"
    saludo = formato_aleatorio().format(nombre)
    return saludo

print(hola("Diego"))