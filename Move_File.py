import os 
import shutil
from_dir="C:/Users/prita/Downloads"
to_dir="C:/Users/prita/OneDrive/Desktop/Destination"
listFiles=os.listdir(from_dir)
print(listFiles)
for filename in listFiles:
    name,extension=os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+filename

        if os.path.exists(path2):
            print("Moving file "+filename+" ...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Creating a Folder")
            print("Moving file "+filename+" ...")
            shutil.move(path1,path3)