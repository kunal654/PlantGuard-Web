from flask import Flask, render_template, request, redirect
import requests
import json


app = Flask(__name__)

url = "https://web-production-904d.up.railway.app/predict/"

def detect(file):
    file = {"file": file}
    response = requests.post(url, files=file)
    result = json.loads(response.text)['class_name']
    return result

# Configurations
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'file' not in request.files:
        return render_template('index.html')
    if request.method == 'POST':
        file = request.files['file']
        result = detect(file)
        return render_template('index.html', prediction=result)
    return render_template('index.html')

@app.route('/whatsapp')
def whatsapp():
    return redirect('https://wa.me/+1(415)523-8886?text=join%20medicine-fine')
@app.route('/developers')
def developers():
    return render_template('developers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  


