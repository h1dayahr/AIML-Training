# print("0 to 9 \n")
# for i in range(10):
#     print(i)
#     print("Welcome")

# print("Printing Numbers from 1 to 10 \n")
# for i in range(1,11):
#     print(i)

# print("Second Example")
# for i in range(1,11):
#     print(i)

# print("Third Example")
# for i in range(11):
#     print(i+1)

# for i in range(5):
#     print(i)
# for i in range(1,5):
#     print(i)
# for item in range(100):
#     print(item-1,end="\t") #\t for tab space

employees=['Raj','Ravi','Sam','Anu','Ri']
for e in employees:
    print(e," ")

employees=['Raj','Ravi','Sam','Anu','Ri']
for e in employees:
    print(e,end="\t")

products=['facewash','sunscreen','facial kit']
for p in products:
    print(p,",",end=".")

for ch in 'Nexperts Academy':
    print(ch,end=" ")
name=input("Enter Your Name: \t")
print('Character of Your Name as Follows: \t')
for ch in name:
    print(ch)

num=int(input('Please enter the number to find out table: \t'))
print(f'Table of Number {num} as follows \n')
for i in range(1,11):
    print(f'{num}*{i}=\t{num*1}')

# num=int(input('Please enter the number to find out table: \t'))
# print(f'Table of Number {num} as follows \t')
# for i in range(11):
#     print(f'{num}*{i}=\t{num*2}')

players=('MSD','VK','KL','RS')
for player in players:
    print(player,end=" ")

# players=('MSD','VK','KL','RS')
# for player in players:
#     print(player[0])

# players=('MSD','VK','KL','RS')
# for player in players:
#     print(player)