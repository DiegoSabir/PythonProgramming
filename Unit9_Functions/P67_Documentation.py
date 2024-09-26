import random
from typing import List, Dict

def formato_aleatorio()->str:
    """
    Retorna un saludo aleatorio formateado con el nombre proporcionado

    Returns:
        str: Saludo aleatorio con el formato adecuado
    """
    formatos = [
        "Hola {}", "Bienvenido",
        "Es genial verte {}",
        "Saludos {}", "Encantado de conocerte"
    ]

    return random.choice(formatos)

def hola(nombre:str)->str:
    """
    Genera un saludo personalizado utilizando un nombre.

    Args:
        nombre (str): Nombre del destinatario del saludo
    
    Returns:
        str: Saludo personalizado
    """
    if nombre == "":
        return "Error: Nombre vacio"
    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres:List)->Dict:
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos

nombres = ["Alex", "Juan", "Carlos", "Pedro"]
print(holas(nombres))