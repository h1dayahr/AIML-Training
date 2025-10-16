#SUPER CLASS/ BASE CLASS/ PARENT CLASS
class Emp:
    def reg(self, id, name):
        self.id=id
        self.name=name

    def display(self):
        print('Id: \t',self.id)
        print('Name: \t',self.name)
#INHERITED CLASS/ DERIVED
class Dev(Emp):
    def Welcome(self):
        print('Welcome to Developer')

d=Dev()
d.Welcome()
d.reg(1,'Max')
d.display()

e=Emp()
e.reg(102,'Del')
e.display