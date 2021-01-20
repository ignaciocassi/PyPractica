"""Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
 also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48"""

x=int(input("Ingrese un número para sumarle 15: "))
lmbda = lambda x:x+15
x=lmbda(x)
print(x)

lmbda2 = lambda x,y:x*y
print(lmbda2(10,10))