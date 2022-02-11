from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__, static_folder="static")


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
