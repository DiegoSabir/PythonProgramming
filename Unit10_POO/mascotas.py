class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def __str__(self) -> str:
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"

class Mascota(Animal):
    def __init__(self, especie, edad, nombre) -> None:
        super().__init__(especie, edad)
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def hablar(self):
        pass

    def __str__(self) -> str:
        return f"Mascota[Nombre: {self.__nombre}, Especie: {self.especie}, Edad: {self.edad}]"
    
class Perro(Mascota):
    def hablar(self):
        return "Woof"

class Gato(Mascota):
    def hablar(self):
        return "Miau"
    
class RegistroMascotas:
    def __init__(self) -> None:
        self.mascotas = []

    def agregar_mascotas(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas(self):
        if self.mascotas:
            print("Lista de mascotas")
            for i, mascota in enumerate(self.mascotas, start = 1):
                print(f"{i}. {mascota}")
        else:
            print("No hay mascotas registradas")

    def editar_mascotas(self, indice, nueva_mascota):
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            self.mascotas[indice] = nueva_mascota

    def eliminar_mascotas(self, indice):
        if indice < 0 or indice >= len(self.mascotas):
            print("No hay registro con ese indice")
        else:
            del self.mascotas[indice]