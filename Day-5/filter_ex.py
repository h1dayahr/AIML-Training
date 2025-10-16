def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2): 
    return num1-num2

def div(num1,num2):
    return num1/num2

print("Welcome to our calculator")
while True:
    print('Select operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit')
    op=int(input('Enter your operation chocie(1-6):\t'))
    if(op==6):
        print('Goodbye')
        break
    if ((op>=6) or (op<=0)):
        print('wrong operation choice, only 1 to 6 are allowed')
        break
    fnum=float(input('Enter first Number:\t'))
    snum=float(input('Enter second Number:\t'))
    if(op==1):
        print('Result after adding:\t',add(fnum,snum))
    elif(op==2):
        print('Result after subtracting:\t',sub(fnum,snum))
    elif(op==3):
        print('Result after multiplying:\t',multi(fnum,snum))
    elif(op==4):
        print('Result after dividing:\t',div(fnum,snum))
    elif(op==5):
        print('Average of {fnum} and {snum}:\t',avg(fnum,snum))
    else:
        print('Wrong operation choice, please choose only 1 to 6')


print("Welcome to our calculator")
while True:
    print('Select operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit')
    op=int(input('Enter your operation chocie(1-6):\t'))
    if(op==6):
        print('Goodbye')
        break
    if ((op>=6) or (op<=0)):
        print('wrong operation choice, only 1 to 6 are allowed')
    else:
        fnum=float(input('Enter first Number:\t'))
        snum=float(input('Enter second Number:\t'))
        if(op==1):
            print('Result after adding:\t',add(fnum,snum))
        elif(op==2):
            print('Result after subtracting:\t',sub(fnum,snum))
        elif(op==3):
            print('Result after multiplying:\t',multi(fnum,snum))
        elif(op==4):
             print('Result after dividing:\t',div(fnum,snum))
        elif(op==5):
             print('Average of {fnum} and {snum}:\t',avg(fnum,snum))
        else:
              print('Wrong operation choice, please choose only 1 to 6')

















 


