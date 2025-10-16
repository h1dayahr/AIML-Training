# print()
# import math
# my_num=int(input('Enter Number to Find Out Square Root: \t'))
# print(f'Square root of {my_num:<10} is: \t',math.sqrt(my_num))

#To  Check Function inside Module
import math
import inspect


# #Get only functions defined in the math module
# functions=inspect.getmembers(math, inspect.isbuiltin)
# print(functions)
# for n, func in functions:
#     print(n)
# print('Sin 90 is:',math.sin(90))

deg=int(input('Degree to find out Cos: \t'))
print(f'Cos\t {deg} is: \t',math.cos(deg))