import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model
with open("beer_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page configuration
st.set_page_config(
    page_title="🍻 Booze Predictor",
    page_icon="🍺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-header {
        font-size: 36px;
        color: #ff6600;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ff6600;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
    }
    .stNumberInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">🍻 Welcome to Booze Predictor 🍻</div>', unsafe_allow_html=True)

# Image
image_path = os.path.join(os.path.dirname(__file__), "images", "beer.jpg")
st.image(image_path, caption="Know your drink levels!", use_column_width=True)

# Input fields in columns
col1, col2, col3 = st.columns(3)
with col1:
    beer = st.number_input("🍺 Beer Servings", min_value=0, max_value=500, value=50)
with col2:
    spirit = st.number_input("🥃 Spirit Servings", min_value=0, max_value=500, value=30)
with col3:
    wine = st.number_input("🍷 Wine Servings", min_value=0, max_value=500, value=20)

# Prediction button
if st.button("Calculate Alcohol Content"):
    features = np.array([[beer, spirit, wine]])
    pred = model.predict(features)
    st.markdown(f"<h3 style='color:green;'>Estimated Total Alcohol: {pred[0]:.2f} litres</h3>", unsafe_allow_html=True)
