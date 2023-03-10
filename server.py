from flask import Flask, render_template, request, make_response, send_file, redirect
import re, base64, os, time, hashlib, datetime


server = Flask(__name__)
acceptedFileExtensions = ["jpg", "peg", "ebp", "fif", "png"]
userIdList = []

@server.route("/")
def index():
    try:
        id = request.cookies["data"]
        if id != "" and id in userIdList:
            if os.path.isfile(os.getcwd()+"/static/results/"+id+"/restored_imgs/"+id+".jpg"):
                return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")
            if os.path.isfile(os.getcwd()+"/static/uploadedImages/"+id+".jpg"):
                return render_template("index.html", isx=True, disableRestoreMemory=False, result=False, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg")
            else:
                response = make_response(render_template("index.html", disableRestoreMemory=True, result=False, uploadedImage = False))
                response.set_cookie("data", '', expires=0)
                return response
        if id != "" and id not in userIdList:
            print(f"Ich sollte nach Daten für {id} schauen")
            response = make_response(render_template("index.html", disableRestoreMemory=True, result=False, uploadedImage = False))
            response.set_cookie("data", '', expires=0)
            return response
    except:
        try:
            rememberMe = request.cookies["rememberMe"]
            return render_template("index.html", unknownUser=False, result=False, uploadedImage = False)
        except:
            return render_template("index.html", unknownUser=True, result=False, uploadedImage = False)

@server.route("/uploadImage", methods=["post", "get"])
def uploadImage():
    if request.method != "POST":
        return "<script>alert(\"Upsi something went wrong\");location.href = \"/\";</script>"
    path = "/static/uploadedImages/"
    try:
        id = request.cookies["data"]
        if os.path.isfile(os.getcwd()+path+id+".jpg"):
            return render_template("index.html", disableRestoreMemory=False, result=False, uploadedImage = True, imagePath=path+id+".jpg")
        return render_template("index.html", result=False, uploadedImage = False)
    except:
        print("BOOOBEARRY")
        id = CreateRandomId()
        userIdList.append(id)
        response = make_response(render_template("index.html", isx=True, disableRestoreMemory=False, result=False, uploadedImage = True, imagePath=path+id+".jpg"))
        response.set_cookie("data", id, max_age=60 * 60 * 1)
        imageFile = request.files["image"]
        fileExtension = re.search("(.{3})\s*$", imageFile.filename)
        if fileExtension.group(1) in acceptedFileExtensions:
            imageFile.save(os.getcwd()+path+id+".jpg")
            return response
        return "<script>alert(\"You have to choose an image file like jpg or png\");location.href = \"/\";</script>"

@server.route("/restoreMemory", methods=["post"])
def restoreMemroy():
    id = request.cookies["data"]
    if os.path.isfile(os.getcwd()+"/static/results/"+id+"/restored_imgs/"+id+".jpg"):
        return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")
    command = f"python3.10 {os.getcwd()}/ai/GFPGAN/inference_gfpgan.py --upscale 2 -i {os.getcwd()}/static/uploadedImages/{id}.jpg -o {os.getcwd()}/static/results/{id}"
    os.system(command)
    return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")    

@server.route("/resetMemory")
def resetMemory():
    try:
        id = request.cookies["data"]
        cmd_deleteUploadedImage = f"del {os.getcwd()}\\static\\uploadedImages\\{id}.jpg"
        clear_folder(f"{os.getcwd()}\\static\\results\\{id}")
        os.system(cmd_deleteUploadedImage)
        os.system(f"rmdir {os.getcwd()}\\static\\results\\{id}")
        response = make_response(render_template("index.html", result=False, uploadedImage = False))
        response.set_cookie("data", '', expires=0)
        return response
    except:
        response = make_response(render_template("index.html", result=False, uploadedImage = False))
        response.set_cookie("data", '', expires=0)
        return response

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

def CreateRandomId():
    return hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()

@server.route("/downloadAiFiles", methods=["get"])
def downloadAiFiles():
    return send_file(os.getcwd()+"/static/downloadableAiFiles/ai.7z")

@server.route("/impressum", methods=["get"])
def impressum():
    return render_template("impressum.html")

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=4747)