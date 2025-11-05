# def factorial(num):
#     if((num==0))or(num==1):
#         return 1
#     else:
#         num=num-1
#         return num*factorial(num-1)
# num=int(input('Enter a number to find out factorial:'))
# print(f'Factorial of {num} is:', factorial(num))

#Python function which converts inches to cm
# 1 inch=2.5cm

# def inches_to_cm(inches):
#     cm = 2.5*inches
#     return cm
# inches=int(input('Enter Inches Value:'))
# print(f'{inches} is equal to {inches_to_cm(inches)} centmeter')
#Write a function to find out the table of given number

def given_number(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*1)}')
number=int(input('Enter Number to find out'))
given_number(number)