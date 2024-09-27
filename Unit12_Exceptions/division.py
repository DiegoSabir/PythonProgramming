try:
    a = int(input("Introduzca el primer numero"))
    b = int(input("Introduzca el segundo numero"))

    resultado = a / b

except ValueError:
    print("Error")

except ZeroDivisionError:
    print("Error")    

except Exception as e:
    print("Error", e)

else:
    print(f"Division entre {a}/{b} = {resultado}")

