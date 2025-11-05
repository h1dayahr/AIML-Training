# print('Sets in Python')
# set_one={'laptop','airphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set_one are:',len(set_one))
# for item in set_one:
#     print(item,end=' ')


#Clear(): Remove all the items from set

# set_one.clear()
# print('\nAfter Clear Number of items on set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

# set_one.remove(item): Update the set and remove item from set

# set_one.remove('airphone')
# print('\nAfter Removing one item from set:',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#Union, Intersaction, Difference
set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}


# #1.UNION                                                #s1.union(s2): Returns a new set with all items from both sets s1,s2
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two)
# print(f'Union of set_one and set_two ad set_three contains: {len(unionset)} following items')
# print(unionset)

#2.INTERSECTION
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'Intersection of set_one and set_two ad set_three contains: {len(newset)} following items')
# print(newset)

#3.DIFFERENCE
print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.difference(set_two)
print(f'difference of set_one and set_two contains: {len(newset)} following items')
print(newset)
