class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=name
    def display(self):
        print('ID: ',self.id)
        print('Name: ',self.name)
        print('Qualification: ',self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual,domain,project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project
    def display(self):
        super().display()
        print('Domain: \t',self.domain)
        print('Project: \t',self.project)

#Qs: Create one Emp object with ID=1, Name='Sam',qual ='MCA'
#Create one Dev object with ID=3, Name='Ravi',qual ='MTech',Project='eShopping',Domain='do not'
#Display Dev Details
#Display Emp Details

# #Employee object
# e1=Emp(1, 'Sam', 'MCA')

# # Developer object
# d1 = Dev(3, 'Ravi', 'MTech', 'do not', 'eShopping')

# # Display Dev details
# print('\nDeveloper Details:')
# d1.display()

# # Display Emp details
# print('\nEmployee Details:')
# e1.display()


#Employee object
e1=Emp()
print('\nEmployee Details:')
e1.display()

# Developer object
d1 = Dev()
print('\nDeveloper Details:')
d1.display()

