def args_func(*args):
    print(args)
print(args_func("Hola", 400, 45.5, True))

def suma(a, b):
    print(f"a = {a} y b = {b}")
    return a + b
print(suma(100, 500))
print(suma(b = 200, a= 700))

def kwargs_func(**kwargs):
    print(kwargs)
print(kwargs_func(nombre = "Alex", a = 100, b = 200))

def argumentos(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
print(argumentos(500, "Hola", True, 400, nombre = "Alex", b = 500))