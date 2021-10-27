from flask import Flask
from flask import render_template
from flask import request, redirect
import os
from os.path import join, dirname, realpath
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

# path = os.join(dirname(realpath(__file__)), 'static/images'
app.config["IMAGE_UPLOADS"] = "static/images"
basedir = os.path.abspath(os.path.dirname(__file__))
@app.route('/upload-image', methods = ["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], image.filename))
            print(image)
            return redirect(request.url)

    return render_template("public/upload_image.html")

@app.route('/upload-video-mob', methods = ["GET", "POST"])
def upload_video():
    if request.method == "POST":
        if request.files:
            print("request files")
            image = request.files["image"]
            # print(image.filename)
            image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], image.filename))
            print(image)
            return redirect(request.url)

    # return render_template("public/upload_image.html")
    return "success"

@app.route('/upload-video', methods = ["GET", "POST"])
def upload_video1():
    if request.method == "POST":
        if request.files:
            print("request files")
            video = request.files["video"]
            # print(image.filename)
            video.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], video.filename))
            print(video)
            return redirect(request.url)

    # return render_template("public/upload_image.html")
    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0")