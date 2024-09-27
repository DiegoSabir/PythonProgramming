from mascotas import *

registro = RegistroMascotas()

while True:
    menu = """--- Menu ---
1. Agregar mascota
2. Listar mascotas
3. Editar mascota
4. Eliminar mascota
5. Salir\n
"""
    opcion = input(menu)
    if opcion == "1":
        nombre =input("Nombre:")
        especie = input("Especie:")
        edad = input("Edad:")

        mascota = Mascota(especie, edad, nombre)
        registro.agregar_mascotas(mascota)

    elif opcion == "2":
        registro.listar_mascotas()

    elif opcion == "3":
        indice = int(input("Indice del registro:"))
        nombre =input("Nombre:")
        especie = input("Especie:")
        edad = input("Edad:")

        nueva_mascota = Mascota(especie, edad, nombre)
        registro.editar_mascotas(indice - 1, nueva_mascota)

    elif opcion == "4":
        indice = int(input("Introduzca el indice de la mascota a eliminar:"))
        registro.eliminar_mascotas(indice)

    elif opcion == "5":
        print("Finalizando")
        break

    else:
        print("Opcion invalida")