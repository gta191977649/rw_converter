import os
import subprocess
TARGET_PLAMFORM = "GTASA"
files = os.listdir('./model')
for file in files: 
    path = './model/'+file
    out = './output/'+file
    print(path)
    subprocess.call(["convdff.exe",'-v '+TARGET_PLAMFORM,path,out])
