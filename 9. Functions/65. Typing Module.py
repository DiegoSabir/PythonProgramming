import random
from typing import List, Dict

def formato_aleatorio() -> str:
    formatos = [
        "Hola {}", 
        "Bienvenido",
        "Es genial verte {}", 
        "Saludos {}", 
        "Encantado de conocerte"
    ]
    return random.choice(formatos)

def hola(nombre: str) -> str:
    if nombre == "":
        return "Error: Nombre vacio"
    
    formato = formato_aleatorio()
    # Solo aplicamos .format() si el formato contiene '{}'
    if '{}' in formato:
        saludo = formato.format(nombre)
    else:
        saludo = formato
    return saludo

def holas(nombres: List[str]) -> Dict[str, str]:
    saludos = {}
    for nombre in nombres:
        saludo = hola(nombre)
        saludos[nombre] = saludo
    return saludos

nombres = ["Alex", "Juan", "Carlos", "Pedro"]
print(holas(nombres))
