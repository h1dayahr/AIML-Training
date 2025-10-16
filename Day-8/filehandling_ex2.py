# #Example 1: Name File to Update
# import os
# # file_path=r'C:\AIML\Day-8\files\sample1.text'
# file_path=os.getcwd()
# filename=input('Enter File Name to Update File: \t ')
# fullpath=os.path.join(file_path,filename)

# if(os.path.exists(fullpath)):
#     file=open(fullpath,'w')
#     content=input('Enter Text to Add in File')
#     file.write(content)
#     print(f'File {filename} updated')
#     file.close()
# else:
#     print(f'No such file {filename} exist') 

#Example 2: Read File
import os
# file_path=r'C:\AIML\Day-8\files\sample1.text'
file_path=os.getcwd()
filename=input('Enter File Name to Read File: \t ')
fullpath=os.path.join(file_path,filename)

if(os.path.exists(fullpath)):
    file=open(fullpath,'r')
    content=file.read()
    print('File Content as Follows')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')