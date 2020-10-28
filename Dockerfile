From tensorflow/tensorflow
RUN pip install pillow && pip install Flask && pip install flask-cors
WORKDIR "/databangla/predict/"
COPY model/model_car_vs_plane.h5 .
COPY script/predict.py .
CMD python predict.py
