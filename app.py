import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=60000, key="refresh")

from weather_service import get_weather_data
from model_service import predict_traffic, predict_flood
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from model import predict_traffic
import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
import base64

# remember login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# LOGIN PAGE
def login_page():

    set_bg("smartcity.jpg")

    st.markdown("<h1 style='text-align:center;color:white;'>Metro Sense</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;color:white;'>Smart City Control Center</h3>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong username or password")



def dashboard():

    st.title("🌆 METRO SENSE – A Smart Urban Intelligence Platform")
    st.info("Real-time AI platform for traffic prediction, flood risk monitoring, and smart infrastructure optimization.")
    st.subheader("AI-driven traffic and urban risk monitoring for Coimbatore")

    col1, col2 = st.columns(2)

    # ---------------- INPUT PANEL ----------------
    with col1:
        st.header("🔧 Traffic Inputs")

        hour = st.slider("Hour of Day", 0, 23, 8)
        rain = st.selectbox("Rain Level", ["No Rain", "Light Rain", "Heavy Rain"])
        event = st.selectbox("Special Event Nearby?", ["No", "Yes"])

        emergency = st.selectbox(
            "Emergency Vehicle Detected?",
            ["None", "Ambulance", "Fire Truck", "Police"]
        )

    # ---------------- PREDICTION PANEL ----------------
    with col2:
        rain_value = {"No Rain": 0, "Light Rain": 1, "Heavy Rain": 2}[rain]
        event_value = {"No": 0, "Yes": 1}[event]

        traffic_score = predict_traffic(hour, rain_value, event_value)

        st.header("📊 Predicted Traffic Level")

        if emergency != "None":
            st.error(f"🚑 EMERGENCY VEHICLE DETECTED: {emergency}")
            st.warning("🚦 Green Corridor Activated")
        elif traffic_score < 30:
            st.success("🟢 Low Traffic")
        elif traffic_score < 60:
            st.warning("🟡 Moderate Traffic")
        elif traffic_score < 80:
            st.error("🔴 High Traffic")
        else:
            st.error("🚨 Critical Congestion")

        st.metric("Traffic Score", traffic_score)

    # ---------------- CONTROL CENTER METRICS ----------------
    st.markdown("---")


    colA, colB, colC, colD = st.columns(4)

    with colA:
        st.metric("🚦 Active Signals", 128)

    with colB:
        st.metric("🚑 Emergency Alerts", 1 if emergency != "None" else 0)

    with colC:
        st.metric("📍 Monitored Intersections", 42)

    with colD:
        st.metric("📊 Avg Traffic Score", round(traffic_score))   

    # ---------------- LIVE WEATHER DATA ----------------
    st.markdown("---")
    st.header("🌦 Live Weather Data – Coimbatore")

    rainfall, temperature, humidity = get_weather_data()

    colW1, colW2, colW3 = st.columns(3)

    with colW1:
        st.metric("🌡 Temperature (°C)", temperature)

    with colW2:
        st.metric("💧 Humidity (%)", humidity)

    with colW3:
        st.metric("🌧 Rainfall (mm)", rainfall)    

    # ---------------- AI DECISION ENGINE ----------------

    st.markdown("---")
    st.header("🌧️ Urban Flood Risk Prediction")

    # Flood risk scoring logic
    flood_score = rainfall * 20 + traffic_score * 0.3 + event_value * 10
    if flood_score < 40:
        st.success("🟢 Low Flood Risk")
    elif flood_score < 70:
        st.warning("🟡 Moderate Flood Risk")
    else:
        st.error("🔴 High Flood Risk")

    # Explanation panel
    st.info(
        "Flood prediction considers rainfall intensity, traffic congestion, "
        "and urban event density to estimate potential drainage overload."
    )

    if emergency != "None":
        st.warning("🚦 Activate GREEN CORRIDOR for emergency vehicle.")
    elif traffic_score > 80:
        st.warning("🚦 Increase signal duration and redirect traffic.")
    elif traffic_score > 60:
        st.info("🚦 Monitor intersection and prepare alternate routes.")
    else:
        st.success("🚦 Traffic flow normal. No intervention needed.")

    # ---------------- FORECAST ENGINE ----------------
    st.markdown("---")
    st.header("📈 AI Traffic Forecast (Next 6 Hours)")

    future_hours = [(hour + i) % 24 for i in range(6)]

    forecast = [
        predict_traffic(h, rain_value, event_value)
        for h in future_hours
    ]

    df = pd.DataFrame({
        "Hour": future_hours,
        "Predicted Traffic": forecast
    })

    fig = px.line(
        df,
        x="Hour",
        y="Predicted Traffic",
        markers=True,
        title="AI Forecast for Next 6 Hours"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- SMART CITY MAP ----------------
    st.markdown("---")
    st.header("🗺 Smart City Traffic Map")

    import streamlit.components.v1 as components

    components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDeAhrGIKzSfpk5vxxKwoM-iNkyt8_aXz0"></script>

    <script>

    function initMap() {

    var coimbatore = {lat: 11.0168, lng: 76.9558};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: coimbatore
    });

    var trafficLayer = new google.maps.TrafficLayer();
    trafficLayer.setMap(map);
    }

    </script>
    </head>

    <body onload="initMap()">

    <div id="map" style="height:500px;width:100%;"></div>

    </body>
    </html>
    """,
    height=520,
    )

    coimbatore_coords = [11.0168, 76.9558]

    m = folium.Map(location=coimbatore_coords, zoom_start=12)
    traffic_points = [
        [11.0168, 76.9558],
        [11.0250, 76.9700],
        [11.0300, 76.9500],
    ]

    from folium.plugins import HeatMap
    HeatMap(traffic_points).add_to(m)

    st_folium(m, width=900, height=500)


    # Flood risk zones (simulated)
    flood_zones = [
        [11.0200, 76.9600],
        [11.0280, 76.9750],
        [11.0150, 76.9900]
    ]

    for zone in flood_zones:
        folium.Circle(
            location=zone,
            radius=500,
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.3,
            popup="🌧️ Flood Risk Zone"
        ).add_to(m)

    # Simulated traffic density data
    traffic_points = [
        [11.0168, 76.9558, 0.9],   # Town Hall (heavy traffic)
        [11.0250, 76.9700, 0.8],   # Gandhipuram
        [11.0300, 76.9800, 0.7],   # Peelamedu
        [11.0120, 76.9900, 0.6],   # Singanallur
        [11.0450, 76.9500, 0.5],   # RS Puram
        [11.0500, 76.9800, 0.4]    # Airport Road
    ]

    HeatMap(traffic_points, radius=25).add_to(m)

    # Accident hotspots
    hotspots = [
        [11.0168, 76.9558],
        [11.0250, 76.9700],
        [11.0300, 76.9800],
        [11.0120, 76.9900]
    ]

    for point in hotspots:
        folium.CircleMarker(
            location=point,
            radius=8,
            color="red",
            fill=True,
            fill_color="red",
            popup="⚠️ Accident Hotspot"
        ).add_to(m)

    # Main city marker
    folium.Marker(
        coimbatore_coords,
        popup="City Traffic Monitoring",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

    # Emergency route
    if emergency != "None":

        route = [
            [11.0168, 76.9558],
            [11.0250, 76.9700],
            [11.0300, 76.9800]
        ]

        folium.PolyLine(
            route,
            color="red",
            weight=5,
            tooltip="Emergency Green Corridor"
        ).add_to(m)

    st_folium(m, width=700, height=500)


    st.markdown("---")
    st.header("⚡ Smart Infrastructure Energy Optimization")

    # Simulated energy consumption model
    active_signals = 128
    base_energy = active_signals * 0.5
    traffic_factor = traffic_score * 0.4
    time_factor = 10 if hour > 18 else 5

    energy_usage = base_energy + traffic_factor + time_factor

    st.metric("Estimated Energy Consumption", f"{round(energy_usage)} kWh")

    # AI recommendation
    if energy_usage < 80:
        st.success("Energy usage within optimal range.")
    elif energy_usage < 120:
        st.warning("Consider reducing signal cycle time during low traffic.")
    else:
        st.error("High energy consumption detected. Activate smart signal optimization.")

    st.markdown("---")
    st.caption("AI-powered urban intelligence prototype for Coimbatore")

if st.session_state.logged_in:
        dashboard()
else:
        login_page()