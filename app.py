import streamlit as st
import pandas as pd
import joblib

# Set page configuration for a professional wide layout
st.set_page_config(
    page_title="Diabetes Classification Dashboard",
    page_icon="🩺",
    layout="wide"
)

# 1. Load the trained model safely with caching
@st.cache_resource
def load_diabetes_model():
    return joblib.load('diabetes_model.pkl')

try:
    model = load_diabetes_model()
except FileNotFoundError:
    st.error("❌ 'diabetes_model.pkl' not found! Please run your training script first to generate the model file.")
    st.stop()

# 2. Setup Headers
st.title("🩺 Medical Diagnosis: Diabetes Prediction Dashboard")
st.write("Enter the patient's demographics and clinical metrics below to predict their classification status.")
st.markdown("---")

# 3. Create Sidebar for Demographic Variables
with st.sidebar:
    st.header("👤 Patient Demographics")
    gender = st.selectbox("Gender", options=["Female", "Male"])
    age = st.number_input("AGE (Years)", min_value=0, max_value=120, value=45, step=1)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=70.0, value=25.4, step=0.1)

# 4. Create Main Body Tabs for Laboratory Panels
st.subheader("🩸 Laboratory & Clinical Profiles")
tab1, tab2 = st.tabs(["🧪 Glycemic & Kidney Function", "🧬 Lipid Profile (Cholesterol)"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        hba1c = st.number_input("HbA1c (%)", min_value=3.0, max_value=20.0, value=5.5, step=0.1, help="Glycated hemoglobin level")
        urea = st.number_input("Urea (mg/dL)", min_value=0.0, max_value=150.0, value=35.0, step=0.1)
    with col2:
        cr = st.number_input("Cr (Creatinine - mg/dL)", min_value=0.0, max_value=15.0, value=0.8, step=0.01)

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        chol = st.number_input("Chol (Total Cholesterol)", min_value=50.0, max_value=500.0, value=170.0, step=1.0)
        ldl = st.number_input("LDL (Low-Density Lipoprotein)", min_value=10.0, max_value=300.0, value=95.0, step=1.0)
    with col2:
        tg = st.number_input("TG (Triglycerides)", min_value=30.0, max_value=600.0, value=125.0, step=1.0)
        vldl = st.number_input("VLDL (Very-Low-Density Lipoprotein)", min_value=5.0, max_value=100.0, value=22.0, step=1.0)
    with col3:
        hdl = st.number_input("HDL (High-Density Lipoprotein)", min_value=10.0, max_value=120.0, value=48.0, step=1.0)

st.markdown("---")

# 5. Prediction Logic
if st.button("📊 Run Diagnostic Classification", type="primary", use_container_width=True):
    
   
    gender_encoded = 1 if gender == "Male" else 0
    
    # Constructing DataFrame
   
    input_data = pd.DataFrame([{
        "Gender": gender_encoded,
        "AGE": age,
        "Urea": urea,
        "Cr": cr,
        "HbA1c": hba1c,
        "Chol": chol,
        "TG": tg,
        "HDL": hdl,
        "LDL": ldl,
        "VLDL": vldl,
        "BMI": bmi
    }])
    
    try:
        prediction = model.predict(input_data)[0]
        
        # Display of Result based on 3 target classes ('N', 'P', 'Y')
        st.subheader("📋 Model Assessment Output")
        
        if prediction == 'Y':
            st.error("⚠️ **Diagnosis Result:** Patient is classified as **Diabetic (Y)**.")
        elif prediction == 'P':
            st.warning("⚡ **Diagnosis Result:** Patient is classified as **Pre-Diabetic (P)**.")
        elif prediction == 'N':
            st.success("✅ **Diagnosis Result:** Patient is classified as **Non-Diabetic (N)**.")
        else:
            st.info(f"ℹ️ **Diagnosis Result:** {prediction}")
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.info("💡 Double check that the columns in your DataFrame are in the exact same sequence as your training dataset variables.")

footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #7f8c8d;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    font-weight: 500;
    border-top: 1px solid #e6e6e6;
    z-index: 100;
}
/* Adjust main content padding so it doesn't get hidden behind footer */
.main .block-container {
    padding-bottom: 60px;
}
</style>
<div class="footer">
    👨‍💻 Created by: <b>RabiMalik</b>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)



