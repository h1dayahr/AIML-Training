# num=1
# print('Printing Numbers from 1 to 100')
# while(num<=100):
#     print(num,end=" ")
#     num+=1

#BREAK EXAMPLE:                       #In break: all numbers listed except those that starts to be divisible by 11/number stated
# num=1
# print('Printing Numbers from 1 to 100 before we get the numbers divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         break
#     print(num,end=" ")
#     num+=1

#CONTINUE EXAMPLE:
# num=1
# while(num<=100):

#     if(num%11==0):
#         num+=1
#         continue
#     print(num,end="\t")     #In Continue: all the numbers listed except the ones that divisible by 11
#     num+=1

# num=1
# while(num<=100):     #If not divisible by number stated, its listed
#         if(num%5==00):
#             num+=1
#             continue
#         print(num,end="\t")
#         num+=1

# for i in range(1,100):       #Only put (...,..) if you want to choose what number to start with
#     if(i%5==0):
#         continue
#     print(i,end="\t")

# #While Loop -Condition arrives unexpectedly Ex: Indefinite
# #Full Loop -We know futher cicumstances Ex: Table of Sifir

# correctPwd='dd031001'
# pwd=input('Enter Password to start Game')
# while True:
#     if(correctPwd==pwd):
#         print('Wrong Password, Try Again')
#         pwd=input('Enter Password to Start the Game')
#         break

# correctPwd='dd031001'
# pwd=input('Enter Password')
# for p in pwd:
#     print(p,end="\t")

# correctPwd='dd031001'
# while True:
#     pwd=input("Enter Password:\t")
#     if(correctPwd==pwd):
#         print('Permission Granted!!')
#         break
#     else: 
#         print('Wrong Password, Try Again')

correctPwd='dd031001'
counter=0
while True:
    pwd=input("Enter Password:\t")
    if(correctPwd==pwd):
        print('Permission Granted!!')
        print('**Game Started**')
        break
    else: 
        print('Wrong Password, Try Again')
        counter+=1
        if(counter>=3):
            print("Blocked for further Attempts")
            break
            