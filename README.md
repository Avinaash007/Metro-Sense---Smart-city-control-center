# Metro sense – Smart Urban Intelligence Platform

## Overview

**Metro sense** is an AI-powered smart city monitoring system that predicts traffic congestion, monitors weather conditions, and identifies potential urban flood risks.
The platform provides real-time insights through an interactive dashboard designed for urban traffic management and smart infrastructure planning.

The system integrates predictive analytics, live weather data, and smart city mapping to help city administrators monitor and optimize urban mobility.

---

## Features

### Smart Login Interface

* Secure login page before accessing the dashboard
* Background smart city interface
* Session-based login control

### AI Traffic Prediction

* Predicts traffic congestion levels using:

  * Time of day
  * Rain conditions
  * Nearby events
* Displays traffic levels:

  * Low
  * Moderate
  * High
  * Critical congestion

### Emergency Vehicle Detection

* Detects emergency vehicles:

  * Ambulance
  * Fire truck
  * Police
* Automatically suggests **Green Corridor Activation**.

### Live Weather Monitoring

Displays real-time weather information:

* Temperature
* Humidity
* Rainfall

Weather data is used to support flood prediction.

### Flood Risk Prediction

The system estimates flood risk using:

* Rainfall intensity
* Traffic congestion levels
* Event density

Flood risk levels:

* Low
* Moderate
* High

### Traffic Forecasting

The AI model predicts **traffic conditions for the next 6 hours** and visualizes it using charts.

### Smart City Traffic Map

Interactive map displaying:

* Traffic density heatmaps
* Accident hotspots
* Flood-prone zones
* Emergency route visualization
* Live traffic layer using Google Maps API

### Smart Infrastructure Energy Optimization

Estimates traffic signal energy usage and provides optimization recommendations.

---

## Technology Stack

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| Python                 | Core programming language |
| Streamlit              | Web dashboard framework   |
| Folium                 | Interactive maps          |
| Plotly                 | Data visualization        |
| Pandas                 | Data processing           |
| Google Maps API        | Live traffic layer        |
| Machine Learning Model | Traffic prediction        |

---

## Project Structure

```
Metro sense
│
├── app.py
├── model_service.py
├── weather_service.py
├── model.py
├── smartcity.jpg
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Avinaash007/Metro sense.git
cd Metro sense
```

### 2. Install Required Libraries

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install folium
pip install streamlit-folium
pip install streamlit-autorefresh
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open the browser at:

```
http://localhost:8501
```

---

## Login Credentials

Default login for demonstration:

```
Username: admin
Password: 1234
```

---

## Use Case

Metro sense can support:

* Smart city traffic management
* Emergency vehicle routing
* Flood risk monitoring
* Urban infrastructure optimization
* City command center dashboards

---

## Future Improvements

Possible extensions include:

* Integration with real-time IoT sensors
* AI accident prediction
* Mobile application integration
* Smart signal automation
* Cloud deployment

---

## Author

Metro sense Smart City Project
Developed as a prototype for intelligent urban monitoring systems.

---
