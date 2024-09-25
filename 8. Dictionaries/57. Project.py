"""
Desarrolla un programa en Python para gestionar un sistema de registro de estudiantes. El sistema debe permitir:
Registro de Estudiantes:
    - Capturar informacion de estudiantes desde la terminal, incluyendo nombre, edad y curso.
    - Almacenar la informacion en un diccionario.

Almacenamiento en una lista:
    - Guardar cada diccionario de estudiante en una lista central.

Visualizacion del registro:
    - Mostrar el registro completo de estudiantes, incluyendo sus detalles como nombre, edad y curso
"""

student_list = []

while True:
    print("---------------------------------------------------------")
    option = int(input("Seleccione una de las siguientes opciones:\n"
          "1. Introducir estudiante\n"
          "2. Listar estudiantes\n"
          "3. Salir\n"
    ))
    print("---------------------------------------------------------")

    if (option == 1):
        name = input("Introduzca el nombre: ")
        age = input("Introduzca la edad: ")
        school_year = input("Introduzca el curso academico: ")
        student = {"Nombre":name, "Edad":age, "Curso":school_year}
        student_list.append(student)

    elif (option == 2):
        print("Lista Estudiantil\n"
              "---------------------------------------------------------")
        for i in student_list:
            print(i)
    
    elif (option == 3):
        print("Finalizando")
        break
