import os
import subprocess

# This example converts dff to GTASA(PC) Engine RW VER: 3.6.0.3
TARGET_PLAMFORM = "d3d9"
TARGET_RW = "36003"
files = os.listdir('./model')
for file in files: 
    path = './model/'+file
    out = './output/'+file
    print(path)
    subprocess.call(["convdff.exe",'-o'+TARGET_PLAMFORM,'-v'+TARGET_RW,path,out])
