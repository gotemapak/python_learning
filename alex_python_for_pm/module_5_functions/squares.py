import python_learning.module_5_functions.functions_refactored as functions_refactored

x = [1, 5, 65, 1, 6]

def square(x):
    return x**2

xx = list(map(lambda x: x**2, x)) #lambda делает тоже самое, 
#                                  что делает def

xx = list(map(square, x)) 

print(xx)

# 1, 25 4225