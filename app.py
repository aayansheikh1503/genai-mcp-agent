import streamlit as st
import requests

st.title("AI Trip Planner Agent 🌍")

prompt = st.text_input("Enter your trip request")

if st.button("Generate Trip Plan"):
    city = "Tokyo"
    
    # 1. City info (LLM-style text)
    st.subheader("About the City")
    st.write(
        "Tokyo is a vibrant city blending ancient temples, imperial history, "
        "and modern technology, making it one of the most culturally rich cities in the world."
    )

    # 2. Weather (real API OR mock)
    st.subheader("Weather")
    st.write("Current Weather: 22°C, Clear Sky")
    st.write("Forecast: Pleasant weather during your trip")

    # 3. Flights (mock)
    st.subheader("Flight Options")
    st.write("• Airline: ANA – ₹45,000 – 7h")
    st.write("• Airline: Japan Airlines – ₹48,000 – 6.5h")

    # 4. Hotels (mock)
    st.subheader("Hotel Options")
    st.write("• Hotel Sakura – ₹6,000/night – ⭐⭐⭐⭐")
    st.write("• Tokyo Inn – ₹4,500/night – ⭐⭐⭐")

    # 5. Trip plan
    st.subheader("3-Day Trip Plan")
    st.write("Day 1: Temples and city exploration")
    st.write("Day 2: Museums and shopping")
    st.write("Day 3: Parks and leisure")
