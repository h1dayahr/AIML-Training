try:
    num1=int(input('Enter 1 Number: \t '))
    num2=int(input('Enter 2 Number: \t '))
    total=num1+num2
    print(f'Sum of {num1} and {num2} = {total}')
except Exception as e:
    print('Error',e)
finally:
    print('End of Program')