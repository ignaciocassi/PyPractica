#Ejercicios de fiunciones Lambdas de W3sSchools https://www.w3resource.com/python-exercises/lambda/index.php

def interseccionEntreListas():
    listaA=[1,2,3,4,5]
    listaB=[3,4,5,6,7]

    interseccion=list(filter(lambda x:x in listaA,listaB))
    return interseccion

def __main__():
    print(interseccionEntreListas())

if __name__=="__main__":
    __main__()