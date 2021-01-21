"""Write a Python program to extract year, month, date and time using Lambda. Go to the editor
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178"""

import datetime

#Sólo la fecha
#from datetime import date
#today=date.today()

def mostrarFechaYHoraAct():
    fechaYHoraActual=datetime.datetime.now()

    year=lambda x:x.year
    month=lambda x:x.month
    day=lambda x:x.day

    año=year(fechaYHoraActual)
    mes=month(fechaYHoraActual)
    dia=day(fechaYHoraActual)

    print(dia)
    print(mes)
    print(año)

def __main__():
    mostrarFechaYHoraAct()

if __name__=="__main__":
    __main__()



