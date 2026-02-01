import streamlit as st
import requests

st.set_page_config(page_title="Lead Conversion Predictor")

st.title("📈 Lead Conversion Prediction")
st.write("Enter lead details to predict conversion probability")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=65, value=30)
website_visits = st.number_input("Website Visits", min_value=0, value=2)
time_spent = st.number_input("Time Spent on Website (seconds)", min_value=0, value=300)
page_views = st.number_input("Page Views per Visit", min_value=0.0, value=2.0)
profile_completed = st.selectbox("Profile Completed", [0, 1, 2], format_func=lambda x: ["Low", "Medium", "High"][x])

print_media_type1 = st.selectbox("Seen Newspaper Ad?", [0, 1])
print_media_type2 = st.selectbox("Seen Magazine Ad?", [0, 1])
digital_media = st.selectbox("Seen Digital Ad?", [0, 1])
educational_channels = st.selectbox("Seen Educational Channels?", [0, 1])
referral = st.selectbox("Referral?", [0, 1])

current_occupation = st.selectbox("Current Occupation", ["Professional", "Student", "Unemployed"])
first_interaction = st.selectbox("First Interaction", ["Website", "Mobile App"])
last_activity = st.selectbox("Last Activity", ["Email Activity", "Phone Activity", "Website Activity"])

# Backend API URL
API_URL = "https://saishdatta-lead-conversion-api.hf.space/predict"

if st.button("Predict Conversion Probability"):
    payload = {
        "age": age,
        "website_visits": website_visits,
        "time_spent_on_website": time_spent,
        "page_views_per_visit": page_views,
        "profile_completed": profile_completed,
        "print_media_type1": print_media_type1,
        "print_media_type2": print_media_type2,
        "digital_media": digital_media,
        "educational_channels": educational_channels,
        "referral": referral,
        "current_occupation": current_occupation,
        "first_interaction": first_interaction,
        "last_activity": last_activity
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Conversion Probability: {result['conversion_probability']}")
    else:
        st.error("Error calling prediction API")