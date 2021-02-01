#Ejercicios de fiunciones Lambdas de W3sSchools https://www.w3resource.com/python-exercises/lambda/index.php

#Ej11
def interseccionEntreListas(listaA=[1,2,3,4,5],listaB=[3,4,5,6,7]):
    interseccion=list(filter(lambda x:x in listaA,listaB))
    print(interseccion)

#Ej12
def ordenarValoresPosNegLista(lista=[1,2,-1,3,-3,5,6,7,-9]):
    result = sorted(lista, key=lambda i: 0 if i == 0 else -1 / i)
    print(result)
    
def __main__():
    #interseccionEntreListas()
    #ordenarValoresPosNegLista()
    

if __name__=="__main__":
    __main__()