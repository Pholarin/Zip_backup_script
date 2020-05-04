#!python3

print("*****Mini FileZipper*****\n\n")
import os
import zipfile
import time
start_op=input("Enter start to begin")
if start_op=="start":
     foldName=time.strftime("%Y%m%d")
     if not os.path.exists("C:\\Users\\name\\Documents\\Python_work\\"+foldName):
        os.mkdir("C:\\Users\\name\\Documents\\Python_work\\"+foldName)


     fileName=time.strftime("%H%M%S")
     oprt=zipfile.ZipFile("C:\\Users\\name\\Documents\\Python_work\\"+foldName+"\\"+fileName+".zip","w")


     for folder,subf,files in os.walk("C:\\Users\\name\\Documents\\Python_work\\ff"):
        for file in files:
            ch=oprt.write(os.path.join(folder,file),os.path.relpath(os.path.join(folder,file),"C:\\Users\\name\\Documents\\Python_work\\"+foldName),compress_type=zipfile.ZIP_DEFLATED)
            print("Compressing",os.path.join(folder,file))
            if ch==None:
                print("Ok!")
            else:
                print("Failed")
     oprt.close()
     print("\nFile saved at:C:\\Users\\name\\Documents\\Python_work\\"+foldName)
     print("\n\n Compression completed!\a")
input("\n\nPress enter to exit")


