#Take user marks from user with 0 to 50.
#if user enter outside [0,50] raise Error invalid marks using custom exception.
#give chance to the user tiill, he/she enters valid marks.

# class InvalidMarks(Exception):
#     pass 
    
# def check_marks(marks):
#     if (marks<0):
#         raise InvalidMarks("Marks should not be negative")
#     elif (marks>=50):
#         raise InvalidMarks("Marks should range 0 to 50")
#     else:
#         print(f'Marks {marks} are valid')

# while True:
#     try:
#         usermarks=int(input("Enter your marks: "))
#         check_marks(usermarks)
#     except InvalidMarks as e:
#         print("Invalid Marks:",e)
#     except Exception as ex:
#         print("Error Occured:",ex)
#     else:
#         print("Thank you for entering valid marks")
#         break
#     choice = input("Do you want to re-enter marks? if yes press y. To exit press any other key: \t").lower()
#     if (choice != 'y'):
#         print("Good Bye!")
#         break
#-------------------------------------------------------------------------------------------------------

from ourpack import mark
while True:
    try:
        usermarks=int(input("Enter your marks: "))
        mark.check_marks(usermarks)
    except mark.InvalidMarks as e:
        print("Invalid Marks:",e)
    except Exception as ex:
        print("Error Occured:",ex)
    else:
        print("Thank you for entering valid marks")
        break
    choice = input("Do you want to re-enter marks? if yes press y. To exit press any other key: \t").lower()
    if (choice != 'y'):
        print("Good Bye!")
        break