# class Player:
#     def __init__(self):
#         print('Welcome to Player Class')

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team
    
#     def display(self):
#         print(f'Id: \t {self.id:<10}\t Name: \t {self.name:<10}\t Team: \t {self.team:>3}')

# #OBJECT CREATION
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,'MSD','Korea')
# p2.reg(2,'Leon','Britain')
# p3.reg(3,'Ali','Egypt')

# p1.display()
# p2.display()
# p3.display()

#PARAMETERIZE CONSTRUCRTION
class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team
    
    def display(self):
        print(f'Id: \t {self.id:<10}\t Name: \t {self.name:<10}\t Team: \t {self.team:>3}')
    def display(self):
        print(f'Id: \t {self.id:<10}\t Name: \t {self.name:<10}\t Team: \t {self.team:>3}')

    def __str__(self):
        return f'{self.id}{self.name}{self.team}'

#OBJECT CREATION
p1=Player(1,'Yoo In','Korea')
p2=Player(2,'Leon','Britain')
p3=Player(3,'Max','Britain')

p1.display()
# p2.display()
# p3.display()

print(p1)
# print(p2)
# print(p3)

