number = 10
print(number)

number2 = "20"
print(number2)

number2 = number2 + number2
print(number2)

type(number)
print(number)

type(number2)
print(number2)

negative_number = -10
print(negative_number)

big_number_v1 = 1000000
big_number_v2 = 1_000_000
print(big_number_v1, "|", big_number_v2)

G = 6.672e-11
ME = 5.96e24
RE = 6375 * 1000
g = (G * ME) / (RE ** 2)
print("Constante de Gravitación Universal:", G, "Masa de la Tierra:", ME, "Radio de la Tierra:", RE, "Gravedad:", g)

import sys
n_min_float = sys.float_info.min
n_max_float = sys.float_info.max
print(n_min_float, "|", n_max_float)

complex_number = 2j + 3j + 2
type(complex_number)
print("Number:", complex_number, "Real Part:", complex_number.real, "Imaginary Part:", complex_number.imag)
