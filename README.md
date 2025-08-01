# 🎓 EduDropout Predictor – Student Dropout Risk Detection using Deep Learning

## 📘 Project Overview
**EduDropout Predictor** is a deep learning-based system designed to predict the likelihood of a student dropping out from an academic program. By analyzing various academic, personal, and institutional factors, this model assists educational institutions in identifying at-risk students early and providing timely support.

This project leverages neural network models to classify whether a student is likely to **continue** or **drop out**, helping reduce attrition rates and improving academic outcomes.

## 📁 Dataset
- **Source:** student dropout dataset.csv
- **Format:** CSV
- **Target Variable:** Dropout (Yes/No or 1/0)

### 🔑 Features Used
- Age, Gender  
- Academic Performance (e.g., GPA, marks)  
- Attendance/Discipline records  
- Financial Support, Family Background  
- Parental Education, Institution Support  
- Course Type, Study Hours  


---

## 🧰 Technologies & Libraries
- **Language:** Python 3  
- **Libraries:**
  - Data Processing: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`
  - Deep Learning: `TensorFlow`, `Keras`

---

## 🚀 Model Workflow

1. **Data Preprocessing**
   - Handling missing values and outliers
   - Normalizing/encoding categorical data
   - Splitting dataset into training and test sets

2. **Exploratory Data Analysis (EDA)**
   - Correlation analysis
   - Visualizations (e.g., dropout vs GPA, dropout by gender)

3. **Model Development**
   - Deep Neural Network (DNN) using TensorFlow/Keras
   - Layer tuning with dropout regularization

4. **Evaluation Metrics**
   - Accuracy
   - Precision, Recall, F1-Score
   - Confusion Matrix

5. **Results**
   - Achieved an overall accuracy of **98%**
   - Visual indicators clearly show dropout-prone student clusters

---

# Future Scope
* Incorporate real-time data integration from student dashboards
* Extend the model to provide dropout reasons and intervention suggestions
* Deploy the solution as a web dashboard using Streamlit or Flask
* Add explainable AI (XAI) techniques for transparent predictions
