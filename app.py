import streamlit as st

# Page config
st.set_page_config(page_title="GenAI MCP Agent", layout="wide")

st.title("🌍 GenAI MCP Agent Assignment")

# Sidebar selector
option = st.sidebar.selectbox(
    "Select Application",
    ["Trip Planner Agent", "Currency & Stock Market Agent"]
)

# =====================================================
# 1️⃣ TRIP PLANNER AGENT
# =====================================================
if option == "Trip Planner Agent":

    st.header("✈️ AI Trip Planner")

    prompt = st.text_input(
        "Enter your trip request (Example: Plan a 3-day trip to Tokyo in May)"
    )

    if st.button("Generate Trip Plan"):

        st.subheader("📍 City Cultural & Historical Significance")
        st.write(
            "Tokyo is the capital of Japan and represents a unique blend of "
            "ancient traditions and modern innovation. From historic temples "
            "like Senso-ji to futuristic districts like Shibuya, the city "
            "reflects Japan’s rich cultural heritage and technological advancement."
        )

        st.subheader("🌤 Current Weather & Forecast")
        st.write("Current Temperature: 22°C")
        st.write("Condition: Clear Sky")
        st.write("Forecast During Trip: Pleasant and mild weather expected.")

        st.subheader("📅 Travel Dates")
        st.write("Suggested Dates: 10 May – 12 May")

        st.subheader("✈️ Flight Options")
        st.write("• ANA Airlines – ₹45,000 – 7 hours")
        st.write("• Japan Airlines – ₹48,000 – 6.5 hours")

        st.subheader("🏨 Hotel Options")
        st.write("• Hotel Sakura – ₹6,000/night – ⭐⭐⭐⭐")
        st.write("• Tokyo Grand Inn – ₹4,500/night – ⭐⭐⭐")

        st.subheader("🗓 3-Day Trip Plan")
        st.write("Day 1: Visit Senso-ji Temple and explore Asakusa district.")
        st.write("Day 2: Explore Shibuya Crossing and Akihabara shopping street.")
        st.write("Day 3: Relax at Ueno Park and visit Tokyo National Museum.")


# =====================================================
# 2️⃣ CURRENCY & STOCK MARKET AGENT
# =====================================================
elif option == "Currency & Stock Market Agent":

    st.header("💱 Currency & Stock Market Agent")

    country = st.text_input(
        "Enter Country Name (Example: Japan / India / USA)"
    )

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

        st.subheader("📊 Major Stock Index")
        st.write("Nikkei 225: 38,200")

        st.subheader("📍 Stock Exchange Headquarters Location")
        st.map({
            "lat": [35.6828],
            "lon": [139.759]
        })
