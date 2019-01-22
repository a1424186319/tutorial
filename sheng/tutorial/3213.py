import os
import os.path
rootdir = "D:/E/wegame/lol"

# file_object = open('train_list.txt','w')

for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        print(f'\r{filename}',end='')

#         file_object.write(filename+ '\n')
# file_object.close()
