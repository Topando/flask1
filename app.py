from flask import Flask, render_template, request, redirect, flash, url_for, session
import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

import requests
import random
UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__, static_folder="static")
picFolder = os.path.join("static", "img")
app.config["UPLOAD_FOLDER"] = picFolder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
dirname = "static/img"


class Form(FlaskForm):
    file = FileField('img', validators=[FileAllowed(['jpg', 'png'])])


@app.route('/', methods=['POST', 'GET'])
def index():
    files = [url_for('static', filename=f"img/{img}") for img in os.listdir(dirname)]
    if request.method == 'GET':

        return render_template('index.html', pictures=files[1:], pictureone=files[0])
    elif request.method == "POST":
        file = request.files['file']
        picture_path = os.path.join('static/img/')
        name = str(random.randint(0, 1000))
        file.save(os.path.join(picture_path, name + '.png'))
        files = [url_for('static', filename=f"img/{img}") for img in os.listdir(dirname)]
        return render_template('index.html', pictures=files[1:], pictureone=files[0])
