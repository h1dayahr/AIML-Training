# import random
# print('Random Number from 1 to 100')
# print(random.randint(1,10))

#EXAMPLE 1 if Python CHOOSE the number
# import random
# name=input('Enter YOur Name: \t')
# luckyNumber=random.randint(1,10)

# print('Welcome Mr\\Ms', name)
# print(f'Your lucky number is: {luckyNumber}')

# if(luckyNumber==1):
#     print(f'Mr\\Ms {name} you have won a Porshce!!')
# elif(luckyNumber==3):
#     print('You won an iPad!!')
# elif(luckyNumber==9):
#     print('You want wireless PowerBank worth RM100!!')
# else:
#     print('Awww :( beter luck next time!')

# #EXAMPLE 2 if Python CHOOSE the number
# import random
# print()
# name = input('Enter Your Name: \t')
# print()
# luckyNumber = int(input('Enter your lucky number (1–10): '))
# print()
# print('Welcome Mr\\Ms', name)
# print()
# if luckyNumber == 1:
#     print(f'Mr\\Ms {name}, you have won a Porsche!!')
# elif luckyNumber == 3:
#     print('You won an iPad!!')
# elif luckyNumber == 9:
#     print('You won a wireless PowerBank worth RM100!!')
# else:
#     print('Awww :( better luck next time!')

#EXAMPLE 3
import random
print()
def findwinner():
    name = input('Enter Your Name: \t')
    print()
    luckyNumber = random.randint(1,10)
    print()
    print(f'Welcome Mr//Ms {name}!! \nCuppon Number: {luckyNumber}')
    if (luckyNumber == 1):
        print(f'Mr\\Ms {name}, you have won a Porsche!!')
    elif luckyNumber == 3:
        print('You won an iPad!!')
    elif luckyNumber == 9:
        print('You won a wireless PowerBank worth RM100!!')
    else:
        print('Awww :( better luck next time!')

