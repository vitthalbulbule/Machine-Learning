import streamlit as st
import pandas as pd
import joblib
import os

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# ==========================================
# LOAD MODEL
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "LinearRegressionModel3.pkl"
)

model = joblib.load(model_path)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background: linear-gradient(
        135deg,
        #dbeafe 0%,
        #f5f3ff 100%
    );
}

/* Main Container */

.main-box {

    background: rgba(255,255,255,0.80);

    backdrop-filter: blur(14px);

    padding: 40px;

    border-radius: 30px;

    box-shadow: 0 10px 35px rgba(0,0,0,0.08);

    margin-top: 20px;
}

/* Title */

.title {

    text-align: center;

    font-size: 48px;

    font-weight: 800;

    color: #111827;

    margin-bottom: 8px;
}

/* Subtitle */

.subtitle {

    text-align: center;

    color: #6b7280;

    font-size: 17px;

    margin-bottom: 35px;
}

/* Link Buttons */

.stLinkButton a {

    background: white !important;

    color: #111827 !important;

    border-radius: 14px !important;

    border: 1px solid #e5e7eb !important;

    font-weight: 600 !important;

    height: 50px !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    transition: 0.3s ease !important;

    text-decoration: none !important;

    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.stLinkButton a:hover {

    background: linear-gradient(
        135deg,
        #ec4899,
        #8b5cf6
    ) !important;

    color: white !important;

    border: none !important;
}

/* Input Labels */

label {

    font-weight: 600 !important;

    color: #111827 !important;
}

/* Predict Button */

.stButton > button {

    width: 100%;

    height: 58px;

    border: none;

    border-radius: 16px;

    background: linear-gradient(
        135deg,
        #ec4899,
        #8b5cf6
    );

    color: white;

    font-size: 20px;

    font-weight: 700;

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.02);
}

/* Result Box */

.result-box {

    background: linear-gradient(
        135deg,
        #10b981,
        #059669
    );

    padding: 25px;

    border-radius: 20px;

    text-align: center;

    color: white;

    font-size: 30px;

    font-weight: 800;

    margin-top: 30px;

    box-shadow: 0 8px 20px rgba(16,185,129,0.25);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# MAIN BOX
# ==========================================

st.markdown(
    "<div class='main-box'>",
    unsafe_allow_html=True
)

# ==========================================
# TITLE
# ==========================================

st.markdown(
    """
    <div class='title'>
        🚗 Car Price Prediction
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
        Machine Learning Web Application
        for Predicting Used Car Prices
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# SOCIAL LINKS
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.link_button(
        "🔗 GitHub Repository",
        "https://github.com/vitthalbulbule/CarPrice-Prediction",
        use_container_width=True
    )

with col2:

    st.link_button(
        "📊 Kaggle Notebook",
        "https://www.kaggle.com/code/vitthalbulbule/predicting-car-price",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# INPUT FIELDS
# ==========================================

Driven_kms = st.number_input(
    "Driven Kilometers",
    min_value=0,
    max_value=500000,
    value=50000,
    step=1000
)

Fuel_Type = st.selectbox(
    "Fuel Type",
    [
        "Petrol",
        "Diesel",
        "CNG",
        "LPG",
        "Electric"
    ]
)

Selling_type = st.selectbox(
    "Selling Type",
    [
        "Dealer",
        "Individual",
        "Trustmark Dealer"
    ]
)

Transmission = st.selectbox(
    "Transmission",
    [
        "Manual",
        "Automatic"
    ]
)

Owner = st.selectbox(
    "Owner",
    [
        0,
        1,
        2,
        3
    ]
)

age = st.slider(
    "Car Age",
    min_value=0,
    max_value=25,
    value=5
)

Present_Price = st.number_input(
    "New Car Price (Lakhs ₹)",
    min_value=0.0,
    max_value=100.0,
    value=8.0,
    step=0.5
)

# ==========================================
# PREDICT BUTTON
# ==========================================

predict = st.button(
    "Predict Car Price 🚀"
)

# ==========================================
# PREDICTION
# ==========================================

if predict:

    input_df = pd.DataFrame({

        'Driven_kms': [Driven_kms],

        'Fuel_Type': [Fuel_Type],

        'Selling_type': [Selling_type],

        'Transmission': [Transmission],

        'Owner': [Owner],

        'age': [age],

        'Present_Price': [Present_Price]
    })

    prediction = model.predict(input_df)

    predicted_price = round(
        prediction[0],
        2
    )

    st.markdown(
        f"""
        <div class='result-box'>

            Estimated Selling Price <br><br>

            ₹ {predicted_price} Lakhs

        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# CLOSE MAIN BOX
# ==========================================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)