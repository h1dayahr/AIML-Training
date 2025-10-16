employee={'id':1,
          'name':'sam',
          'salary':55000.50
        }
 
# print('employees details as follows')
# for key, value in employee.items():
#     print(key,"->",value)

# employee['city']='muscat'
# print('\nDictionary after adding city\n')

# for key,value in employee.items():
#     print(key,"->",value)

# del employee['salary']
# print("\nEmployee Details after deleting Salary \n")
# for key,value in employee.items():
#     print(key,"->",value)

#DICTIONARY FUNCTIONS
#1.subject.values()     <---
employee={'id':1,
          'name':'sam',
          'salary':55000.50
        }
print('All keys from Employee')
for k in employee.values():
    print(k,end='\t')

#2.subject.v=items()
# print('\nKey:\t value \n')
# for k,v in employee.items():
#     print(k,":",v)

print('\nDictionary as follows')
print(employee)