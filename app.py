import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("student_model.pkl")

# 🎨 Streamlit page config
st.set_page_config(page_title="🎓 Student Performance Predictor", page_icon="📊", layout="centered")

# Title
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>📚 Student Exam Score Predictor</h1>
    <p style='text-align: center; color: gray;'>Enter details below to predict final exam score</p>
    """,
    unsafe_allow_html=True,
)

# Sidebar info
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    "This app predicts student exam performance based on study habits, attendance, "
    "parental involvement, and lifestyle factors."
)

# Input form
with st.form("prediction_form"):
    st.subheader("✏️ Enter Student Details")

    hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    parental = st.slider("Parental Involvement (1-5)", 1, 5, 3)
    resources = st.slider("Access to Resources (1-5)", 1, 5, 3)
    extra = st.radio("Extracurricular Activities", [0, 1], index=0, help="0 = No, 1 = Yes")
    sleep = st.number_input("Sleep Hours per Day", min_value=0, max_value=12, value=7)

    submitted = st.form_submit_button("🔮 Predict Score")

# Prediction
if submitted:
    features = np.array([[hours, attendance, parental, resources, extra, sleep]])
    prediction = model.predict(features)[0]

    st.success(f"🎯 Predicted Exam Score: **{prediction:.2f}** / 100")
