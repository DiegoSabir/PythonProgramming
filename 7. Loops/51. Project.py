"""
Genera un numero aleatorio entre 1 y 100
El usuario debe ingresar un numero con un limite de 10 intentos
Debe ayudar al usuario en cada intento
Muestra el resultado de si ganaste o perdiste
"""
import random
secret_number = random.randint(1, 100)
counter = 10

for i in range(10):
    number = int(input("Introduzca un numero: "))
    counter -= 1

    if (number == secret_number):
        print("Adivinaste el numero")
        if (counter == 9):
            print("Con el 1º intento")
        else:
            print("Te quedaban", counter, "intentos")
        break
    
    elif(number != secret_number and counter == 0):
        print("Se te acabaron los intentos, el numero secreto era ", secret_number)
        
    else:
        if (number < secret_number):
            print("El numero secreto es mayor a", number)
        else:
            print("El numero secreto es menor a", number)
        print("Te quedan", counter, " intentos")

