# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self,amount):
#         self.bal+=amount

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print('Balance after Withdraw: \t ',self.bal)
#         else:
#             print('Insufficient Amount in Account')
#             print('Transaction Failed!!')
#     def show(self):
#         print(f'Account Holder Name: \t {self.ac_holder:<10} Account Balance: \t {self.bal:>3}')

# ac1=Account('DD',50000)
# ac2=Account('Max',14000)
# ac1.show()
# ac2.show()

# ac1=Account('Dd',50000)
# ac1.show()
# wamount=float(input('Enter Amount to Withdraw : \t'))
# ac1.withdraw(wamount)

#Example2
# class Account:
#     def __init__(self,balance,ac_holder):
#         self.balance=balance
#         self.ac_holder=ac_holder
        
#     def get_balance(self):
#         return self.balance

# acc=Account(1000,'Sam')
# acc.balance=34000
# print(acc)

###
class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print('Balance After Deposit:',self.bal)
    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after Withdraw: \t ',self.bal)
        else:
            print('Insufficient Amount in Account')
            print('Transaction Failed!!')
    def show(self):
        print(f'Account Holder Name: \t {self.ac_holder:<10} Account Balance: \t {self.bal:>3}')

ac=Account('Dd',15000)
ac.show()

while True:
    op=int(input('\nChoose Number: \n1.Deposit \n2.Withdrawal \n3.Exit'))
    if(op==3):
        print('Thank You')
        break
    else:
        if(op==1):
            amount=int(input('Inser Amount: \n'))
            ac.deposit(amount)
            break
        if(op==2):
            amount=int(input('Inser Amount: \n'))
            ac.deposit(amount)
            break        
        else:
            print('Choose Only Provided')