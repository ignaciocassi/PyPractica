def crearListaNumeros():
    lista=[]
    numero=int(input("Ingrese un número para agregarlo a la lista: "))
    while numero!=-1:
        lista.append(numero)
        numero=int(input("Ingrese un número para agregarlo a la lista: "))
    return lista

def filtrarNumerosLista(lista):
    numerosPares,numerosImpares=[],[]
    for numero in lista:
        if numero%2==0:
            numerosPares.append(numero)
        else:
            numerosImpares.append(numero)
    return numerosPares,numerosImpares

def __main__():
    lista=crearListaNumeros()
    numerosPares,numerosImpares=filtrarNumerosLista(lista)
    print(" ")
    print("Lista original: ")
    print(lista)
    print(" ")
    print("Lista de numeros pares: ")
    print(numerosPares)
    print(" ")
    print("Lista de números impares: ")
    print(numerosImpares)
    print(" ")

if __name__=="__main__":
    __main__()