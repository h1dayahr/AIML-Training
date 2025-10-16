import datetime
import inspect
dtclasses=inspect.getmembers(datetime,inspect.isclass)
print()
print('All Classes in datetime module: \t ')
for n in dtclasses:
    print(n,end='\t')
print()
print('\n-----Calling-----')
print(datetime.date.today())
print()
print('----Today----\n')
print(datetime.date.today())
print()
print('----Current Time----\n')
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S %p')

print('Current Time: \t ',cttime)
print('Formated Time: \t ',formatedtime)