def display():
    print('Welcome to Recap of Function')

def welcome(name):
    print('Welcome to functions Mr/Ms',name)

def cube(num):
    cube_num=num*num*num
    print(f'Cube of given Number:{num} is =\t {cube_num}')

def square(num):
    return num*num
username=input('Enter User Name: \t')
my_num=int(input('Enter number to find out cube and square: \t'))

welcome(username)
cube(my_num)
sqnum=square(my_num)
print(f'Square of {my_num} is: {sqnum}')

def salBonus(salary):
    return salary*0.10
    print(f'Salary {salary} Bonus: {bonus}')
    
my_sal=float(input('Enter Salary to find out bonus: \t'))
salBonus(my_sal)
print(f'Salary after bonus =\t')


# my_sal=int(input('Enter Salary'))
# bonus=salBonus(my_sal)
# print(f'Salary {my_sal} Bonus: {bonus}')
# print('Salary after Bonus=\t',(my_sal+bonus))

#Example2
# welcome(username)
# cube(my_num)
# sqnum=square(my_num)
# print(f'Square of {my_num} is: {sqnum}')
# print(f'Number: {my_num} Square: {sqnum}')

# welcome('sam')
# display()
# my_num=int(input('Enter Number to find out Cube:'))
# cube(my_num)


