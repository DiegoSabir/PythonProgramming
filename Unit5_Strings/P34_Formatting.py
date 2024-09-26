name = "Juan"
age = 30
height = 1.80

#
message = "Hola, me llamo %s, tengo %d y mido %.2f metros" % (name, age, height)

#
message2 = "Hola, me llamo {}, tengo {} y mido {:.2f} metros".format(name, age, height)

#
message3 = f"Hola, me llamo {name}, tengo {age} y mido {height:.2f} metros"

print(message)
print(message2)
print(message3)