#EXAMPLE1
# import os
# file_path=r'C:\AIML\Day-8\files\sample1.text'
# file=open(file_path,'w')
# content=input('Enter Text to Write in File')
# file.write(content)
# file.close()

#Example 2: To Create File
import os
# file_path=r'C:\AIML\Day-8\files\sample1.text'
file_path='C:\\AIML\\Day-8\\files'
filename=input('Enter File Name to Create File: \t ')
fullpath=os.path.join(file_path,filename)
file=open(fullpath,'w')
content=input('Enter Text to Write in File')
file.write(content)
print(f'File {filename} created at {fullpath} and content saved in file')
file.close()

#EXAMPLE3