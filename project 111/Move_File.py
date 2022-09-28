import os 
import shutil

from_dir = "C:/Users/ASUS/Downloads"
to_dir = "C:/Users/ASUS/Desktop/download images"

list_of_files = os.list(from_dir)
#print(list_of_files)



for file_name in list_of_files:
    name,extension= os.path.splitest(file_name)
    print(name)
    print(extension)


    if extension in value:
                file_name = os.path.basename(event.scr_path)

                print("Download"+ file_name)

              
                path1 = from_dir + '/' + file_name

                path2 = to_dir + '/' + key

                path3 = to_dir + '/' + key + '/' + file_name



                path1 = from_dir+'/'+file_name
                path2 = to_dir +'/'+key
                path3 = to_dir+'/'+key +'/'+file_name



    else:
        print("making directory...")
        os.makedirs(path2)
        print("moving" + file_name + "....")
        shutil.move(path1,path2)


        shutil.move(path1, path3)