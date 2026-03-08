import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Create synthetic dataset
np.random.seed(42)

data_size = 500

hour = np.random.randint(0, 24, data_size)
rain = np.random.randint(0, 3, data_size)  # 0: No rain, 1: Light, 2: Heavy
event = np.random.randint(0, 2, data_size) # 0: No event, 1: Event

traffic_score = (
    hour * 2 +
    rain * 15 +
    event * 20 +
    np.random.normal(0, 5, data_size)
)

df = pd.DataFrame({
    "hour": hour,
    "rain": rain,
    "event": event,
    "traffic_score": traffic_score
})

X = df[["hour", "rain", "event"]]
y = df["traffic_score"]

model = RandomForestRegressor()
model.fit(X, y)

def predict_traffic(hour, rain, event):
    input_data = pd.DataFrame([[hour, rain, event]],
                              columns=["hour", "rain", "event"])
    prediction = model.predict(input_data)
    return round(float(prediction[0]), 2)