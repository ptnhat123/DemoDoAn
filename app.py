from flask import Flask, request, jsonify, render_template
import pytesseract
from PIL import Image
import io
import os

app = Flask(__name__)

# Cấu hình đường dẫn Tesseract (CHỈ DÙNG KHI CHẠY LOCAL)
tesseract_cmd = os.environ.get("TESSERACT_CMD", "tesseract")  
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(img)
    return jsonify({"result": text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway cấp port tự động
    app.run(host="0.0.0.0", port=port)
