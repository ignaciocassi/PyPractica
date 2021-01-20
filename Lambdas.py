#Función normal:

x=1

print("Función normal: ")

def funcion(x):
    return x+x

x=funcion(x)
print(x)

#Función lambda
#No tienen nombre
#Pueden tener sólo una expresión en su cuerpo
#No tienen un return porque el cuerpo se devuelve automáticamente

print("Función lambda")

#Hay que llamarla mediante la referencia porque sigue siendo una función
lmbda = lambda x : x+1
print(lmbda(x))


