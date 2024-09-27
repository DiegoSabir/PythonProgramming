import datetime as dt
#from datetime import *
#from datetime import date, datetime as d
#from datetime import datetime, datetime as dt

hoy = dt.date.today()
ahora = dt.datetime.now()

print(hoy, "|", ahora)

from my_package.module1 import saludar
#from my_package import module1
from colorama import init, Fore

if __name__ == "__main__":
    saludar()
    print(__name__)
    print(Fore.RED + "Mensaje en rojo")
    print(Fore.GREEN + "Mensaje en verde")
    print(Fore.BLUE + "Mensaje en azul")
