import os

'''

f= open('practice.txt','w+')
f.write('this is a test string')
f.close
import os

print(os.getcwd())

x =(os.listdir('/home/threat_hunter/Desktop/python_practice/oop/advance'))
for i in x:
        
    print(i)
       

import shutil
shutil.move('practice.txt','/home/threat_hunter/Desktop/python_practice/oop/advance/test1folder/')


# to delete 
# os.unlink(path)
# os.rmdir(path)
#shutil.rmtree(path) safe to use send2trash

import send2trash

f= open('test.txt','w+')
f.write('this is a test string')
f.close

send2trash.send2trash('/home/threat_hunter/Desktop/python_practice/oop/advance/test.txt')
print(os.listdir())
'''

#tuple unpacking
file_path = os.getcwd()
for folders, sub_folders,files in os.walk(file_path):

    print(f'Currently looking at {folders}')
    print('\n')
    print(f'The subfolders are:')
    for sub_fold in sub_folders:
        print(f'\tSubfolder: {sub_fold}')
    
    print('\n')
    print(f'The files are:')
    for f in files:
        print(f'\tFiles: {f}')



    









