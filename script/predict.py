import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Flatten, Conv2D,MaxPool2D,Activation, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import models , layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import Flask
from flask import request
import PIL
from PIL import Image
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route("/hello/")
def hello():
    d = {}
    d["user"] = "John Doe"
    d["age"]  = 27
    d["cars"] = [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    return d

@app.route("/hellox/", methods=['GET', 'POST'])
def hellox():
    d = {}
    d["user"] = "John Doe2"
    d["age"]  = 27
    d["cars"] = [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    return d
@app.route("/predict/", methods=['GET', 'POST'])
def predict():
    file = request.files['file']
    d = {}
    #test_image = image.load_img('car1.jpg', target_size=(64, 64))
    #test_image = image.img_to_array(test_image)
    test_image = Image.open(file)
    test_image = test_image.resize((64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model1.predict(test_image)
    
    if result[0][0] == 0.0:
       d["category"] = "car"
    if result[0][0] == 1.0:
       d["category"] = "plane"
    
    return d

if __name__ == '__main__':
    model1 = tf.keras.models.load_model('model_car_vs_plane.h5')
    model1.summary()
    app.run(debug=True, host='0.0.0.0', port=80)

