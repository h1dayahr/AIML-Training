print("List Example One")

my_list=[10,20,30,"Python",None,True,False, 12.45,'Ravi']
print('Number of items in list are:',len(my_list))
for item in my_list:
    print(item)                            #len(...) <--- function to count the items in list



# print('Second Example of List')
# emps=['DD','Tasya','Fatiah']
# print('Number of Employees:',len(emps))
# print('All Employees')
# for emp in emps:
#     print(emp)

# print(emps)

# for emp in emps:
#     print(emp,end=" ")    

# for emp in emps:
#     print(emp, )
    
#     print('List after Sorting')              #To sort list alphabet by sequence
# for e in emps:
#     print(e,end="\n")mps.sort()


#Reverse Example
#ListName.reverse()
# emps.reverse()
# print('Employees in Descending Order')      #To sort list in desending
# for e in emps:
#     print(e,end=" ")

#------------------------------------------------------------------------------------------------------------------------------

# emps=['dd','tasya','fatiah','irfan','maira','dede','sa','max',]
# print('Number of Employees:',len(emps))
# for e in emps:
#     print(e,end="\n")

#1.APPEND:                                                                          #Add the item at the end of the list
# newEmp=input('\nEnter Employees Name to Add in list')
# emps.append(newEmp)
# print('\nAfter adding New Employee: Number of Employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

# #2.INSERT:                                                              #(index,item):This will add item at the particular/selected index
# newEMp=input("\nEnter employee name to add in list: \t")
# pos=int(input("\nEnter position where you want to insert inside list:\t"))
# emps.insert(pos,newEMp)
# print('\nAfter adding New Employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

#3.REMOVE:                                                                #Will remove item from the list
# delEmp=input('\nEmployee to remove from the list:\t')
# emps.remove(delEmp)
# print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#3.1REMOVE(To remove Item that arent in the list)
# delEmp=input('\nEmployee to remove from the list:\t')
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
#     for emp in emps:
#      print(emp,end="\n")
# else:
#     print(f'No such item {delEmp} exist')

#4.LISTNAME.POP(Index)                                              #Will delete element at given index and return its value
# del_index=int(input('Enter Index to pop item:\t'))
# print('Pop Result: ',emps.pop(del_index))

# print('Number of Employees after pop() are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

emps=['dd','tasya','fatiah','irfan','maira','dede','sa','max',]
print('Number of Employees:',len(emps))
for e in emps:
    print(e,end="\n")
count=len(emps)
print('\n First Element of Employees List is: ',emps[0])
print('\n Last Element of Employees List is: ',emps[-1])
print('\n Second Element of Employees List is: ',emps[-2])
print('\n Last Element of Employees List is: ',emps[count-1])
