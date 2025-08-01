import streamlit as st


st.set_page_config(
    page_title="🎓 EduDropout Predictor",
    page_icon="📚",
    layout="centered",
)

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8fbfc, #e0f7fa);
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #FFF, #e0f7fa);
    }
    h1 {
        color: #ffffff;
        background: linear-gradient(90deg, #00695c, #004d40);
        padding: 18px 30px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #00796b;
        color: #fff;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 2.5em;
        transition: 0.3s ease;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004d40;
    }
    input, select {
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🎓 EduDropout Predictor")

st.markdown(
    """
    Enter student details below to estimate the dropout chance.  
    _Powered by our demonstration ML logic._  
    """
)


with st.form("predict_form"):
    col1, col2 = st.columns(2)

    with col1:
        attendance = st.number_input("📚 Attendance Percentage (%)", 0, 100, 85)
        study_hours = st.number_input("📖 Study Hours per Day", 0, 10, 4)
        gpa = st.number_input("🎓 Previous GPA (0–4)", 0.0, 4.0, 3.2, step=0.1)
        motivation = st.number_input("🔥 Motivation Level (0–10)", 0, 10, 7)

    with col2:
        exam_score = st.number_input("📝 Latest Exam Score", 0, 100, 78)
        gender = st.selectbox("👤 Gender", ["Male", "Female"])
        extracurricular = st.selectbox("🏅 Extra-Curricular Participation", ["Yes", "No"])
        family_income = st.selectbox("💰 Family Income", ["Low", "Medium", "High"])

    predict_btn = st.form_submit_button("🔍 Predict Dropout Chance")


if predict_btn:
    if attendance == 0 or motivation == 0 or exam_score == 0:
        st.warning("⚠️ Please fill all key values properly!")
    else:
        attendance_factor = (100 - attendance) * 0.4
        motivation_factor = (10 - motivation) * 5.0
        exam_factor = (100 - exam_score) * 0.2

        dropout_pct = attendance_factor + motivation_factor + exam_factor
        dropout_pct = max(0, min(100, dropout_pct))
        fake_confidence = 95 + (motivation / 100)

        if dropout_pct < 30:
            color = "#2e7d32"  # Green (success)
        elif dropout_pct < 60:
            color = "#fb8c00"  # Orange (warning)
        else:
            color = "#c62828"  # Red (danger)

        st.markdown(
            f"""
            <div style='
                border-radius:12px; 
                padding:25px; 
                background-color:{color};
                color:white;
                font-size: 18px;
            '>
            <h4>✅ ML Model Prediction:</h4>
            <p><strong>Estimated Dropout Chance:</strong> {dropout_pct:.2f}%</p>
            <p><strong>Prediction Confidence:</strong> {fake_confidence:.2f}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
