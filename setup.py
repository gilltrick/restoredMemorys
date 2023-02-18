'''
Download the AI from: https://restorememory.gilltrick.com/downloadAiFiles
and extract the file
or execute this setup file
'''

import os, requests, py7zr

print(f"Check for dependencis")
os.system(f"python -m pip install -r requirementes.txt")
print(f"Dependencies installed")

def downloadAiFiles():
    file = requests.get("https://restorememory.gilltrick.com/downloadAiFiles").content
    f = open(os.getcwd()+"/ai.7z", "wb")
    f.write(file)
    with py7zr.SevenZipFile(os.getcwd()+"/ai.7z", mode='r') as z:
        z.extractall()

def aiInstalled():
    if os.path.isdir(f"{os.getcwd()}/ai"):
        if os.path.isdir(f"{os.getcwd()}/gfpgan"):
            return True
        
if not aiInstalled:
    print(f"AI not installed. Try to download and setting up AI")
    downloadAiFiles()
else:
    print(f"Starting webserver")    
    os.system(f"python {os.getcwd()}/server.py")