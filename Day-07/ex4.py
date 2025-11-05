# import os
# import inspect

# print()
# print ('Current Directory: \t ',os.getcwd())
# print('\nLogin Name: \t ',os.getlogin())

# # functions=inspect.getmembers(os,inspect.isbuiltin)

# # print('All Function is OS Module: \t ')
# # for n in functions:
# #     print(n)

# #EXAMPLE: To Create a folder inside current Directory w Python
import os
cdri=os.getcwd()

# print()

# folder_name=input('Enter Folder Name to Create: \t ')
# folder_path=os.path.join(cdri,folder_name)
# print()
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} Created at {folder_path}')

#QS.1: Write code to Rename a folder
#os.rename(folder_name, 'renamed_folder')
print()
folder_name=input('Enter New Folder Name: \t ')
folder_path=os.path.join(cdri,folder_name)
print()
if(os.path.exists(folder_path)):
    print('Folder Exist, Try New Name')
    new_name=input('New Name: \t ')
    new_folder_path = os.path.join(cdri, new_name)
    os.makedirs(new_folder_path, exist_ok=True)
    print(f'{new_name} created at {new_folder_path}')
else:
    os.makedirs(folder_path,exist_ok=True)
    print(f'{folder_name} Created at {folder_path}')

#EXAMPLE 2
