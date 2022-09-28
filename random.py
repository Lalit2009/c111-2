import os
import shutil
from_directory="C:/Users/vasan/Downloads"
to_director=""
listoffiles=os.listdir(from_directory)
print(listoffiles)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    print(extension)
    print(name)
