# 2.MAP() FUNCTION Example; To find out odd or even number
numbers=[10,25,30,40,2,1]
double_num= list(map(lambda x: 2*x, numbers))
print()
print("Original List")
for num in numbers:
    print(num,end=" ")

print()

print('Double List')
for num in double_num:
    print(num,end=" ",)

# #Example1(FILTER in DICTIONARY): Write Code Using filter to find out all the Number less than 5
# # our_list=[4,2,5,6,7,3,1,10]
# # less_than5= list(filter(lambda x: x<5, our_list))

# # print("Original List")
# # for num in less_than5:
# #     print(num, end=" ")

# # print('\nNew List as Follows\n')
# # for num in our_list:
# #     print(num,end=" ")

# #Example2:      [0]          [1]  
# # #  
# students_marks={'Dd ':60, 
#                 'Irfan':28,
#                 'Del':35,
#                 'Max':45,
#                 'Conrad':76,
#                 'Belly':40,
#                 'Leon':54,
#                 }
# print()            
# print('All Students')
# for k,v in students_marks.items():
#     print(f'Name: \t {k:<10} -> \t Marks: \t {v:>3}')   
# #{subejct:<10} <- left align {subject:>3} <- right ali
# #  ][65gn

# print()
# pass_student=dict(filter(lambda i: i[1]>= 50, students_marks.items()))
# print()
# print('Pass Student')
# for k,v in pass_student.items():
#     print(f'Name: \t {k:<10} -> \t Marks: \t {v:>3}')

#EXAMPLE IN  #In Asecending order
# sort_pass_student=sorted(pass_student.items(), key=lambda x:x[1])    #In Asecending order
# print('Asending Order')
# print(sort_pass_student)

#EXAMPLE IN  #In decending order
# sort_pass_student_desc=sorted(pass_student.items(), key=lambda x:x[1],reverse=True)    #In decending order
# print('Desending Order')
# print(sort_pass_student_desc)

#Example to make it A TABLE
# students_marks={'Dd ':60, 
#                 'Irfan':55,
#                 'Del':35,
#                 'Max':45,
#                 'Conrad':76,
#                 'Belly':40,
#                 'Leon':54,
#                 }
# print()
# def print_table(title, data):
#     print(f"{title}")
#     print("=" * 30)
#     print(f"{'Name':<12} | {'Marks':>5}")
#     print("-" * 30)
#     for k, v in data.items():
#         print(f"{k:<12} | {v:>5}")
#     print("=" * 30)
# print_table('All Student', students_marks)

# pass_student=dict(filter(lambda i: i[1]>= 50, students_marks.items()))
# print()
# def print_table(title, data):
#     print(f"{title}")
#     print("=" * 30)
#     print(f"{'Name':<12} | {'Marks':>5}")
#     print("-" * 30)
#     for k, v in data.items():
#         print(f"{k:<12} | {v:>5}")
#     print("=" * 30)
# print_table('Pass Student', pass_student)

#EXAMPLE 3
# students_marks={'Dd ':60, 
#                 'Irfan':55,
#                 'Del':35,
#                 'Max':45,
#                 'Conrad':76,
#                 'Belly':40,
#                 'Leon':54,
#                 }
# print()            
# print('All Students')
# for k,v in students_marks.items():
#     print(f'Name: \t {k:<10} -> \t Marks: \t {v:>3}')   
# #{subejct:<10} <- left align {subject:>3} <- right align

# print()
# pass_student=dict(filter(lambda i: i[1]>= 50, students_marks.items()))
# print()
# print('Pass Student')
# for k,v in pass_student.items():
#     print(f'Name: \t {k:<10} -> \t Marks: \t {v:>3}')
# sort_wdict=sorted(pass_student.items(), key=lambda x:x[1])    #In Asecending order
# print(sort_wdict)

# sort_pass_student=dict(sorted(pass_student.items(), key=lambda x:x[1]))    #In Asecending order
# print('Asending Order')
# print(sort_pass_student)