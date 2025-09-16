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
    initial_sidebar_state="collapsed"
)

# Styling code (keep it from previous step)
st.markdown(""" 
<style>
    .stApp {
        background-color: #1a1a1a;
        color: #f0f0f0;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .main-header {
        font-size: 40px;
        color: #00ccff;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #00ccff;
        color: #1a1a1a;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 28px;
        font-size: 18px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0099cc;
    }
    .stNumberInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #333;
        background-color: #2b2b2b;
        color: #fff;
        padding: 10px;
    }
    .stNumberInput label {
        color: #ccc;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">🍻 Booze Predictor 🍻</div>', unsafe_allow_html=True)

# Image
image_path = os.path.join(os.getcwd(), "images", "cool_beer.jpg")
if os.path.exists(image_path):
    st.image(image_path, caption="Cheers to knowing your limits!", use_column_width=True)
else:
    st.error("Image not found! Please upload 'images/cool_beer.jpg'.")

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    beer = st.number_input("🍺 Beer Servings", min_value=0, max_value=500, value=50)
with col2:
    spirit = st.number_input("🥃 Spirit Servings", min_value=0, max_value=500, value=30)
with col3:
    wine = st.number_input("🍷 Wine Servings", min_value=0, max_value=500, value=20)

# Prediction
if st.button("Calculate Alcohol Content"):
    features = np.array([[beer, spirit, wine]])
    pred = model.predict(features)
    st.markdown(f"<h3 style='color:#00ccff;'>Estimated Total Alcohol: {pred[0]:.2f} litres</h3>", unsafe_allow_html=True)
