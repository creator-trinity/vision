from flask import Flask, render_template, redirect, url_for, request, flash
import os
from werkzeug.utils import secure_filename
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


UPLOAD_FOLDER = 'E:/AAYUSH TECH/Projects/vision/static/DetectionImages'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ext = str(secure_filename(file.filename)).split(".")[1]
            current_time = datetime.datetime.now()
            filename = str(current_time.microsecond) + "." + ext
            basedir = os.path.abspath(os.path.dirname(__file__))
            img_loc = os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename)
            print(img_loc)
            file.save(img_loc)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)