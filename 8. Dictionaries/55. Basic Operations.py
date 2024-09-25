dictionary1 = {"nombre":"Juan", "edad":30 , "ciudad":"Madrid"}

dictionary1["clave1"] = "valor1"

dictionary1.update({"clave2":"valor2"})
dictionary1.update({"clave3":"valor3"})
dictionary1.update({"clave4":"valor4"})

del dictionary1["clave4"]
dictionary1.pop("clave3")

len(dictionary1)

list(dictionary1.keys())
list(dictionary1.values())
list(dictionary1.items())
