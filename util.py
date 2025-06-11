import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

LABELS = ['CARDBOARD', 'GLASS', 'METAL', 'PAPER', 'PLASTIC', 'TRASH']

def load_classification_model(model_path='EcoUrban.h5'):
    return load_model(model_path)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(300, 300))
    img_array = image.img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def predict_image(model, img_array):
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    predicted_class = LABELS[class_index]
    return predicted_class, confidence