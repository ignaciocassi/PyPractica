"""Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""

def crearListaDiccionario():
    lista=[]
    dicc=dict()
    marcaact=input("Ingrese la marca del celular: ")
    while marcaact!="-1":
        dicc["marca"]=marcaact
        dicc["modelo"]=int(input("Ingrese el modelo del celular: "))
        dicc["color"]=input("Ingrese el color del celular: ")
        lista.append(dicc)
        dicc=dict()
        marcaact=input("Ingrese la marca del celular: ")
    return lista

def ordenarListaDiccionariosConLambda(lista):
    listaOrdenada=sorted(lista,key=lambda lista:lista["modelo"],reverse=True)
    return listaOrdenada

def __main__():
    lista=crearListaDiccionario()
    listaOrdenada=ordenarListaDiccionariosConLambda(lista)
    print(listaOrdenada)

if __name__=="__main__":
    __main__()
