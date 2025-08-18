import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ------------------------------
# Load Models
# ------------------------------
import os
import joblib


# Get base directory (ui/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the models folder (one level up from ui/)
MODELS_DIR = os.path.join(BASE_DIR, "..", "models")

# Final model path
model_path = os.path.join(MODELS_DIR, "RandomForest_full_pipeline.pkl")

# Load pipeline
rf_pipeline = joblib.load(model_path)


# ------------------------------
# Page Layout
# ------------------------------
st.markdown("<h1 style='text-align: center; color: darkblue;'>❤️ AI Heart Disease Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Powered by Random Forest AI Model</p>", unsafe_allow_html=True)

# ------------------------------
# Sidebar Inputs
# ------------------------------
st.sidebar.header("Patient Information")
age = st.sidebar.number_input("Age", 1, 120, 50)
sex = st.sidebar.selectbox("Sex (1=Male, 0=Female)", [1,0])
cp = st.sidebar.selectbox("Chest Pain Type (1=typical, 2=atypical, 3=non-anginal, 4=asymptomatic)", [1,2,3,4])
trestbps = st.sidebar.number_input("Resting Blood Pressure", 50, 200, 120)
chol = st.sidebar.number_input("Cholesterol", 100, 400, 200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
restecg = st.sidebar.selectbox("Resting ECG (0=normal,1=ST-T abnormality,2=LVH)", [0,1,2])
thalach = st.sidebar.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.sidebar.selectbox("Exercise Induced Angina (0=No,1=Yes)", [0,1])
oldpeak = st.sidebar.number_input("ST Depression (oldpeak)", 0.0, 10.0, 1.0, 0.1)
slope = st.sidebar.selectbox("Slope of Peak ST Segment (1=upsloping,2=flat,3=downsloping)", [1,2,3])
ca = st.sidebar.selectbox("Number of Major Vessels Colored", [0,1,2,3])
thal = st.sidebar.selectbox("Thalassemia (3=normal,6=fixed defect,7=reversible defect)", [3,6,7])

# ------------------------------
# Main Button
# ------------------------------
if st.button("Predict Heart Risk"):
    # Input DataFrame
    input_data = pd.DataFrame({
        "age":[age],"sex":[sex],"cp":[str(cp)],"trestbps":[trestbps],
        "chol":[chol],"fbs":[str(fbs)],"restecg":[str(restecg)],
        "thalach":[thalach],"exang":[str(exang)],"oldpeak":[oldpeak],
        "slope":[str(slope)],"ca":[str(ca)],"thal":[str(thal)]
    })

    # Prediction
    
    prediction = rf_pipeline.predict(input_data)
    prediction_proba = rf_pipeline.predict_proba(input_data)[:,1]
    risk = prediction_proba[0]

    # ------------------------------
    # Layout Columns
    # ------------------------------
    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Prediction Result")
        if risk >= 0.5:
            st.markdown(f"<h2 style='color:red;'>❤️ Heart Disease Risk: YES</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color:green;'>❤️ Heart Disease Risk: NO</h2>", unsafe_allow_html=True)
        st.write(f"Probability: {risk:.2f}")
        st.progress(risk)

        # Pie Chart
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie([risk,1-risk], labels=['Risk','No Risk'], autopct='%1.1f%%', colors=['red','green'], startangle=90)
        ax.set_title("Heart Disease Probability", fontsize=16)
        st.pyplot(fig, use_container_width=True)

    with col2:
        st.subheader("AI Model Info")
        st.markdown("""
        - **Model:** Random Forest Classifier  
        - **Features:** Age, Sex, Chest Pain, BP, Cholesterol, etc.  
        - **Accuracy:** ~93%
        - **Precision:** ~96%
        - **Recall:** ~88%
        - **F1-score:** ~91%           
        - **Purpose:** Predicts risk of heart disease based on patient data
        """)
        st.info("💡 This prediction is AI-based and for informational purposes only. Consult a doctor for medical advice.")

    # Show input data below
    st.subheader("Input Data Summary")
    st.dataframe(input_data)
