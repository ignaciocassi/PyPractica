#Write a Python program to find whether a given string starts with a given character using Lambda.
from Práctica.Ej8PrácticaW3s import mostrarFechaYHoraAct

def obtenerCadena():
    while True:
        try:
            cadena=input("Ingrese una cadena: ")
            break
        except TypeError:
            print("Debe ingresarse una cadena, reintente... ")
    return cadena
        
def __main__():
    cadena=obtenerCadena()
    verificarPrefijo=lambda cadena:True if (cadena.startswith("P")) else False

    if(verificarPrefijo(cadena)):
        print("La cadena empieza con P.")
    else:
        print("La cadena no empieza con P.")

    print(mostrarFechaYHoraAct())

if __name__=="__main__":
    __main__()