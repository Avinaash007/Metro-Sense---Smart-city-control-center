import joblib
import numpy as np

# Load trained models
traffic_model = joblib.load("models/traffic_model.pkl")
flood_model = joblib.load("models/flood_model.pkl")

# Traffic prediction
def predict_traffic(hour, day_of_week, temp, rain, snow):

    features = np.array([[hour, day_of_week, temp, rain, snow]])
    prediction = traffic_model.predict(features)

    return int(prediction[0])

# Flood prediction
def predict_flood(rainfall, elevation):

    features = np.array([[rainfall, elevation]])
    prediction = flood_model.predict(features)

    return int(prediction[0])