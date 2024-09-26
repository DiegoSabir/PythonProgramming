class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"

class Mascota(Animal):
    def __init__(self, especie, edad, nombre) -> None:
        super().__init__(especie, edad)
        self.nombre = nombre

    def hablar(self):
        pass

    def __str__(self) -> str:
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"
    
class Perro(Mascota):
    def hablar(self):
        return "Woof"

class Gato(Mascota):
    def hablar(self):
        return "Miau"
    
p = Perro("Perro", "1 Año", "Bobby")
g = Gato("Gato", "6 Meses", "Pelusa")

print(p.hablar())
print(g.hablar())