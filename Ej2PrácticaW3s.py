"""Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number. Go to the editor
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75"""

from random import randint

lmbda = lambda x:x*randint(2,5)

numero = lmbda(10)
print(numero)