import streamlit as st
import numpy as np
import joblib

# =========================
# LOAD MODEL & SCALER
# =========================
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

st.set_page_config(page_title="Dropout Prediction", layout="centered")

st.title("🎓 Student Dropout Prediction")
st.write("Sistem prediksi risiko mahasiswa dropout")

# =========================
# INPUT USER
# =========================
st.subheader("📋 Input Data Mahasiswa")

age = st.number_input("Age at Enrollment", 17, 60, 20)
admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)
prev_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0, 110.0)

sem1_grade = st.number_input("Curricular Units 1st Sem Grade", 0.0, 20.0, 12.0)
sem2_grade = st.number_input("Curricular Units 2nd Sem Grade", 0.0, 20.0, 12.0)

sem1_approved = st.number_input("1st Sem Approved Units", 0, 20, 5)
sem2_approved = st.number_input("2nd Sem Approved Units", 0, 20, 5)

debtor = st.selectbox("Debtor", [0, 1])
tuition = st.selectbox("Tuition Fees Up To Date", [0, 1])
scholarship = st.selectbox("Scholarship Holder", [0, 1])

# =========================
# INPUT ARRAY (WAJIB URUT SESUAI TRAINING)
# =========================
input_data = np.array([[
    age,
    admission_grade,
    prev_grade,
    sem1_grade,
    sem2_grade,
    sem1_approved,
    sem2_approved,
    debtor,
    tuition,
    scholarship
]])

# =========================
# SCALING
# =========================
input_scaled = scaler.transform(input_data)

# =========================
# PREDICTION
# =========================
if st.button("🔍 Predict"):

    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][1]

    st.subheader("📊 Hasil Prediksi")

    if prediction == 1:
        st.error(f"⚠️ Risiko Dropout Tinggi ({proba:.2%})")
    else:
        st.success(f"✅ Tidak Berisiko Dropout ({proba:.2%})")

    # =========================
    # INSIGHT SIMPLE RULE-BASED
    # =========================
    st.markdown("### 💡 Insight")

    if sem1_grade < 10 or sem2_grade < 10:
        st.write("- Performa akademik rendah meningkatkan risiko dropout")

    if debtor == 1:
        st.write("- Status hutang meningkatkan risiko dropout")

    if tuition == 0:
        st.write("- Tunggakan biaya kuliah menjadi faktor risiko tambahan")

    if scholarship == 1:
        st.write("- Penerima beasiswa cenderung lebih aman dari risiko dropout")
