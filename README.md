# EcoUrban Waste Classification ♻️

## Project Overview
EcoUrban Waste Classification is a web application designed to help users identify and classify different types of waste materials: Cardboard, Glass, Metal, Paper, Plastic, and Trash. By leveraging a deep learning model (built with TensorFlow/Keras), the application provides quick and accurate predictions, promoting better waste management and recycling practices.

The project features a simple Flask web interface for image uploads and a dedicated API endpoint for programmatic access, making it versatile for both direct user interaction and integration into other systems.

## ✨ Features
- **Waste Image Classification**: Upload an image of waste and get an instant prediction of its category.
- **Confidence Score**: See the confidence level of each prediction.
- **User-Friendly Web Interface**: A simple and intuitive web page for easy interaction.
- **RESTful API Endpoint**: Programmatic access for integrating the classification service into other applications.
- **Scalable**: Built on Flask and TensorFlow, ready for deployment.

## � Technologies Used
- **Python**: The core programming language.
- **Flask**: Web framework for building the application's backend and serving the web interface.
- **TensorFlow / Keras**: Deep learning framework for the classification model.
- **Numpy**: For numerical operations, especially with image data.
- **Pillow (PIL Fork)**: For image preprocessing (loading, resizing).
- **Werkzeug**: WSGI utility library used by Flask.

## 📦 Installation (Local Setup)
To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/anurag232s2/EcoUrban.git
   cd EcoUrban
