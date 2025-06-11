from flask import Flask, request, render_template, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import util

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model once at startup
try:
    model = util.load_classification_model()
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if model is None:
            return render_template('index.html', prediction="Model not loaded", error=True)
            
        if 'image' not in request.files:
            return render_template('index.html', prediction="No image uploaded", error=True)

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', prediction="No image selected", error=True)

        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Predict
            img_array = util.preprocess_image(filepath)
            predicted_class, confidence = util.predict_image(model, img_array)

            return render_template(
                'index.html',
                prediction=predicted_class,
                confidence=round(confidence * 100, 2),
                filename=filename,
                success=True
            )
        except Exception as e:
            return render_template('index.html', prediction=f"Error processing image: {str(e)}", error=True)

    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # API endpoint for Postman users
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
        
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected"}), 400

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        img_array = util.preprocess_image(filepath)
        predicted_class, confidence = util.predict_image(model, img_array)

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": round(confidence * 100, 2),
            "filename": filename,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)