from flask import Flask, render_template, request, make_response, send_file
import re, base64, os, time, hashlib, datetime


server = Flask(__name__)

@server.route("/")
def index():
    try:
        id = request.cookies["data"]
        if id != "":
            if os.path.isfile(os.getcwd()+"/static/results/"+id+"/restored_imgs/"+id+".jpg"):
                return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")
            if os.path.isfile(os.getcwd()+"/static/uploadedImages/"+id+".jpg"):
                return render_template("index.html", disableRestoreMemory=False, result=False, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg")
            else:
                return render_template("index.html", disableRestoreMemory=False, result=False, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg")
    except:
        return render_template("index.html", result=False, uploadedImage = False)

@server.route("/uploadImage", methods=["post"])
def uploadImage():
    path = "/static/uploadedImages/"
    try:
        id = request.cookies["data"]
        if os.path.isfile(os.getcwd()+path+id+".jpg"):
            return render_template("index.html", disableRestoreMemory=False, result=False, uploadedImage = True, imagePath=path+id+".jpg")
        return render_template("index.html", result=False, uploadedImage = False)
    except:
        id = CreateRandomId()
        response = make_response(render_template("index.html", disableRestoreMemory=False, result=False, uploadedImage = True, imagePath=path+id+".jpg"))
        response.set_cookie("data", id)
        imageFile = request.files["image"]
        if imageFile.filename == "":
            return render_template("index.html", result=False, uploadedImage = False)
        imageFile.save(os.getcwd()+path+id+".jpg")
        return response

@server.route("/restoreMemory", methods=["post"])
def restoreMemroy():
    id = request.cookies["data"]
    if os.path.isfile(os.getcwd()+"/static/results/"+id+"/restored_imgs/"+id+".jpg"):
        return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")
    command = f"python3.10 {os.getcwd()}/ai/GFPGAN/inference_gfpgan.py --upscale 2 -i {os.getcwd()}/static/uploadedImages/{id}.jpg -o {os.getcwd()}/static/results/{id}"
    os.system(command)
    return render_template("index.html", disableRestoreMemory=True, result=True, uploadedImage = True, imagePath="/static/uploadedImages/"+id+".jpg", resultImagePath="/static/results/"+id+"/restored_imgs/"+id+".jpg")    

@server.route("/resettMemory")
def resettMemory():
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