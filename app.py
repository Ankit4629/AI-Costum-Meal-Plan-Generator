import streamlit as st
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Setup Streamlit UI
st.title("🥗 AI Custom Meal Plan Generator")
st.write("Get a personalized meal plan based on your preferences.")

# User inputs
goal = st.selectbox("What's your goal?", ["Weight loss", "Muscle gain", "Maintenance"])
diet = st.selectbox("Diet preference", ["No preference", "Vegetarian", "Vegan", "Keto", "Non-veg"])
calories = st.slider("Daily calorie target", 1200, 4000, 2000, step=100)
meals = st.slider("How many meals per day?", 1, 6, 3)

if st.button("Generate Meal Plan"):
    with st.spinner("Cooking up your plan..."):
        try:
            # Create prompt
            prompt = (
                f"Create a {meals}-meal-per-day meal plan for someone with the goal of {goal.lower()}, "
                f"following a {diet.lower()} diet and targeting {calories} calories per day. "
                "Include meal names and brief descriptions."
            )

            # Load model and generate content
            model = genai.GenerativeModel(model_name="models/gemini-2.0-flash" )
  # Fallback model
            response = model.generate_content(prompt)
            st.success("Here's your meal plan:")
            st.markdown(response.text)

        except Exception as e:
            st.error("⚠️ Something went wrong while generating the meal plan.")
            st.exception(e)
