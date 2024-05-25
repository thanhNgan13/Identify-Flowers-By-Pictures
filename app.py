from flask import Flask, render_template, request, jsonify, url_for
from PIL import Image
import os
import numpy as np
import tensorflow as tf
import requests
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tải mô hình
model = tf.keras.models.load_model('best_model_flower.h5', compile=False)
class_labels = [
    'calla_lily', 'daisy', 'dandelion', 'frangipani', 'hibiscus', 
    'lotus', 'orchid', 'rose', 'sunflower', 'tulip'
]
THRESHOLD = 0.5  # Ngưỡng xác suất để chấp nhận dự đoán

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    image_path = None
    error = None

    # Nếu người dùng tải lên một file
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)
        image_url = url_for('static', filename='images/' + file.filename)

    # Nếu người dùng nhập một đường dẫn URL
    elif 'url' in request.form and request.form['url'] != '':
        url = request.form['url']
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_name = 'temp_image.jpg'
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
                img = Image.open(BytesIO(response.content))
                img.save(image_path)
                image_url = url_for('static', filename='images/' + image_name)
            else:
                error = f"Error: Unable to fetch image. HTTP Status code: {response.status_code}"
        except Exception as e:
            error = str(e)

    if image_path and not error:
        try:
            prediction = predict_image(image_path)
            return jsonify({'image_url': image_url, 'prediction': prediction})
        except Exception as e:
            error = str(e)

    return jsonify({'error': error})

def predict_image(image_path):
    try:
        img = Image.open(image_path).convert('RGB').resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        max_prob = np.max(predictions)
        if max_prob < THRESHOLD:
            return "Unable to identify"
        predicted_class = class_labels[np.argmax(predictions)]
    
        return predicted_class
    except Exception as e:
        print(f"Error processing image: {e}")
        return "Unable to identify"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
