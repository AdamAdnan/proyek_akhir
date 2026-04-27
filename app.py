import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

st.set_page_config(page_title="Dropout Prediction", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎓 Student Dropout Prediction</h1>", unsafe_allow_html=True)
st.write("")

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📋 Input Data Mahasiswa")

    col1, col2 = st.columns([1,1])

    with col1:
        age = st.number_input("Age at Enrollment", 17, 60, value=17)
        admission_grade = st.number_input("Nilai Masuk", 0.0, 200.0, value=0.0)
        sem1_grade = st.number_input("Nilai Semester 1", 0.0, 20.0,  value=0.0)
        sem2_grade = st.number_input("Nilai Semester 2", 0.0, 20.0,  value=0.0)
        debtor = st.selectbox("Status Hutang (Debitur)", [0, 1])

    with col2:
        prev_grade = st.number_input("Nilai Kualifikasi Sebelumnya", 0.0, 200.0,  value=0.0)
        sem1_approved = st.number_input("Jumlah Mata Kuliah Lulus Semester 1", 0, 20,  value=0)
        sem2_approved = st.number_input("Jumlah Mata Kuliah Lulus Semester 2", 0, 20,  value=0)
        tuition = st.selectbox("Pembayaran UKT Lancar", [0, 1])
        scholarship = st.selectbox("Penerima Beasiswa", [0, 1])

    input_data = np.array([[
    prev_grade,
    admission_grade,
    debtor,
    tuition,
    scholarship,
    age,
    sem1_approved,
    sem1_grade,
    sem2_approved,
    sem2_grade
    ]])

    input_scaled = scaler.transform(input_data)

    predict_button = st.button("🔍 Predict")

with right_col:
    st.subheader("📊 Hasil Prediksi")

    if predict_button:
        prediction = model.predict(input_scaled)[0]
        proba = model.predict_proba(input_scaled)[0][1]

        if prediction == 1:
            st.error(f"⚠️ Risiko Dropout Tinggi\n\nProbabilitas: {proba:.2%}")
        else:
            st.success(f"✅ Tidak Berisiko Dropout\n\nProbabilitas: {proba:.2%}")

        st.markdown("### 💡 Insight")

        if sem1_grade < 10 or sem2_grade < 10:
            st.write("- Nilai akademik rendah meningkatkan risiko dropout")

        if debtor == 1:
            st.write("- Status hutang meningkatkan risiko")

        if tuition == 0:
            st.write("- Tunggakan biaya kuliah menjadi faktor risiko")
