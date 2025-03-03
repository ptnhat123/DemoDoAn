from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(img)
    return {"result": text}

if __name__ == '__main__':
    app.run(debug=True)
