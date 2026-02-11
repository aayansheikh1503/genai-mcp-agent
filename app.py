import streamlit as st
import requests

st.title("AI Trip Planner Agent 🌍")

prompt = st.text_input("Enter your trip request")

if st.button("Generate Trip Plan"):
    city = "Tokyo"import streamlit as st

st.set_page_config(page_title="GenAI MCP Agents", layout="wide")

st.title("🌍 GenAI MCP Agent Assignment")

option = st.sidebar.selectbox(
    "Choose Application",
    ["Trip Planner Agent", "Currency & Stock Market Agent"]
)

# =========================
# TRIP PLANNER
# =========================
if option == "Trip Planner Agent":
    st.header("✈️ AI Trip Planner")

    prompt = st.text_input("Enter your trip request (Example: Plan a 3-day trip to Tokyo in May)")

    if st.button("Generate Trip Plan"):
        st.subheader("📍 About the City")
        st.write(
            "Tokyo is a vibrant metropolis blending ancient temples, imperial history, "
            "and futuristic technology. It represents Japan’s rich cultural heritage "
            "while being one of the world’s most modern cities."
        )

        st.subheader("🌤 Current Weather")
        st.write("Temperature: 22°C")
        st.write("Condition: Clear Sky")
        st.write("Forecast: Pleasant weather expected during your trip.")

        st.subheader("✈️ Flight Options")
        st.write("• ANA Airlines – ₹45,000 – 7h")
        st.write("• Japan Airlines – ₹48,000 – 6.5h")

        st.subheader("🏨 Hotel Options")
        st.write("• Hotel Sakura – ₹6,000/night – ⭐⭐⭐⭐")
        st.write("• Tokyo Inn – ₹4,500/night – ⭐⭐⭐")

        st.subheader("🗓 3-Day Trip Plan")
        st.write("Day 1: Visit Senso-ji Temple and explore Asakusa.")
        st.write("Day 2: Explore Shibuya Crossing and shopping districts.")
        st.write("Day 3: Relax at Ueno Park and visit museums.")


# =========================
# CURRENCY & STOCK AGENT
# =========================
elif option == "Currency & Stock Market Agent":
    st.header("💱 Currency & Stock Market Details")

    country = st.text_input("Enter Country Name (Example: Japan)")

    if st.button("Get Details"):
        st.subheader("💰 Official Currency")
        st.write("Japanese Yen (JPY)")

        st.subheader("💱 Exchange Rates (1 JPY)")
        st.write("USD: 0.0067")
        st.write("INR: 0.56")
        st.write("GBP: 0.0053")
        st.write("EUR: 0.0061")

        st.subheader("📈 Major Stock Exchange")
        st.write("Tokyo Stock Exchange (TSE)")

        st.subheader("📊 Stock Index Value")
        st.write("Nikkei 225: 38,200")

        st.subheader("📍 Stock Exchange Location")
        st.map({"lat": [35.6828], "lon": [139.759]})

    
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

