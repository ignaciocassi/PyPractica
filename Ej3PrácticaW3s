""" Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

def crearListaTuplas():
    lista=[]
    materia=input("Ingrese la materia: ")
    while(materia!="-1"):
        numero=int(input("Ingrese el número: "))
        lista.append((materia,numero))
        materia=input("Ingrese la materia: ")
    return lista

lt = crearListaTuplas()
lt.sort(key=lambda x:x[1])

print(lt)