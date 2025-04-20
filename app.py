import streamlit as st
import google.generativeai as genai

# Load API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.title("🥗 AI Custom Meal Plan Generator")

st.write("Get a personalized meal plan based on your preferences.")

# User input
goal = st.selectbox("What's your goal?", ["Weight loss", "Muscle gain", "Maintenance"])
diet = st.selectbox("Diet preference", ["No preference", "Vegetarian", "Vegan", "Keto", "Paleo"])
calories = st.slider("Daily calorie target", 1200, 4000, 2000, step=100)
meals = st.slider("How many meals per day?", 1, 6, 3)

if st.button("Generate Meal Plan"):
    with st.spinner("Cooking up your plan..."):
        prompt = (
            f"Create a {meals}-meal-per-day meal plan for someone with the goal of {goal.lower()}, "
            f"following a {diet.lower()} diet and targeting {calories} calories per day. "
            "Include meal names and brief descriptions."
        )
        response = model.generate_content(prompt)
        st.success("Here's your plan:")
        st.markdown(response.text)
