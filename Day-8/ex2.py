from ourpack import calc
try:
    fnum=float(input('Enter First Number: \t '))
    print()
    snum=float(input('Enter Second Number: \t '))
    print()
    op=input('Choosee Operation: \t +,-,*,/')


    print()

    if(op=='+'):
        print('Result: \t',calc.add(fnum,snum))
    elif(op=='-'):
        print('Result: \t',calc.sub(fnum,snum))
    elif(op=='*'):
        print('Result: \t',calc.multi(fnum,snum))
    elif(op=='/'):
        print('Result: \t',calc.div(fnum,snum))
    else:
        print('Wrong Operation Choice')
except ZeroDivisionError as ze:
    print('Division by 0 is not allowed')
except ValueError as ve:
    print('Error in Values:',ve)
except Exception as e:
    print('Error!!,',e)
