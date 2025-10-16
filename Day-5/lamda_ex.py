# def add(a,b):
#     total= a+b
#     return
# result=add(12,15)
# print(result)

# ad=lambda a, b: a + b
# multi=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:(a-b)

# num1=int(input('Enter first Number: \t'))
# num2=int(input('Enter first Number: \t'))
# print()

# print("Multiplication Result: ",multi(num1,num2))
# print("Sutraction Result: ",sub(num1,num2))

# check_even=lambda x: "even" if x % 2 == 0 else "odd"

#1.LAMBDA FUNCTION Example; To find out odd or even number
check_odd= lambda n: "odd number" if n%2==1 else "even number"
num1=int(input('Enter Number to check Odd or Even: \t'))
print(check_odd(num1))

