import os, time, sys

USERLIST = []

def clear_folder(dir):
    if os.path.exists(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                else:
                    clear_folder(file_path)
                    os.rmdir(file_path)
            except Exception as e:
                print(e)

def removeUserData(id):
    clear_folder(f"{os.getcwd()}\\static\\results\\{id}")
    os.system(f"del {os.getcwd()}\\static\\uploadedImages\\{id}.jpg")
    os.system(f"rmdir {os.getcwd()}\\static\\results\\{id}")

def init():
    uploadedImageList = os.listdir(os.getcwd()+"/static/uploadedImages")
    for image in uploadedImageList:
        print(f"Path: {os.getcwd()}/static/uploadedImages/{image}")
    print(f"[CLEANER] {str(len(uploadedImageList))} files in uploadedImages folder")
    oldUsers = os.listdir(f"{os.getcwd()}/static/results/")
    for user in oldUsers:
        removeUserData(user)

def Clean():
    uploadedImageList = os.listdir(os.getcwd()+"/static/uploadedImages")
    for image in uploadedImageList:
        print(f"Path: {os.getcwd()}/static/uploadedImages/{image}")    
    yn = input("Delete those files? [y/n]: ")
    if yn == "y":
        for image in uploadedImageList:
            os.system(f"del {os.getcwd()}\\static\\uploadedImages\\{image}")
        init()
        print("Everything should be gone")
    else:
        print("Do nothing")
    print("Done")


def loop():
    while True:
        init()
        time.sleep(60*60)

def Run(command):
    if command ==  "loop":
        loop()
    if command == "--clean":
        Clean()


if __name__ == "__main__":
    try:
        command = sys.argv[1]
    except:
        command = ""
    Run(command)