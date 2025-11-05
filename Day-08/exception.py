try:
    fnum=float(input('Enter First Number: \t '))
    print()
    snum=float(input('Enter Second Number: \t '))
    print()
    result=fnum/snum
    print()
    print(f'Result After Dividing {fnum} by {snum} is:{round(result,4)}')
    print()    
except Exception as e:
    print('Error',e)
    print()
finally:
    print('Goodbye')