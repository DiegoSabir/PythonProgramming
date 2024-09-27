try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()

except FileNotFoundError:
    print("El archivo no se ha encontrado")
    print("Creando archivo")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Hola Mundo")

else:
    print("Contenido del archivo:\n",
        contenido
    )

finally:
    if archivo:
        archivo.close()
