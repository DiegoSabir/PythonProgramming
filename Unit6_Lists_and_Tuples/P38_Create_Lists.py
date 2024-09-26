colors = ["rojo", "verde", "azul", "amarillo"]

print(colors[0], colors[2])

print(colors[-1], colors[-3])

print(len(colors))

colors[0] = "Rojo"
colors[-4] = "rojo"

if("rojo" in colors):
    colors.append("blanco")
    colors.extend(["negro", "marron", "morado"])
    colors.remove("marron")

print(colors)