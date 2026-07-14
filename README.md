# 🩺 Diabetes Classification & Diagnostic Dashboard:
A production ready interactive streamlit web application built with scikit learn to predict clinical diabetes status.
The caore system utilizes "Decision Tree Classifier" trained on patient clinical metrics to categorize individual into three distinct groups: Non-Daibetic, Pre-Diabetic, and Diabetic.

**Live App Link:**
*[https://diabetes-predictionsapp.streamlit.app/]*

## 🛠️ Data Features & Clinical Metrics
The predictive system uses the following 11 features extracted from patient records:
* `Gender` (Encoded as Male: 1, Female: 0)
* `AGE` (Patient age in years)
* `Urea` (Blood urea level)
* `Cr` (Creatinine level)
* `HbA1c` (Glycated hemoglobin percentage)
* `Chol` (Total cholesterol level)
* `TG` (Triglycerides level)
* `HDL` (High-Density Lipoprotein)
* `LDL` (Low-Density Lipoprotein)
* `VLDL` (Very-Low-Density Lipoprotein)
* `BMI` (Body Mass Index)

## 📊 Model Evaluation & Performance

The engine is built using an optimized **Decision Tree Classifier** (`max_depth=5`). The model achieves high accuracy and clinical sensitivity on unseen test frameworks.

### 📈 Key Metrics
* **Overall Model Accuracy:** `98.40%`
* **Test Dataset Distribution:** 250 clinical patient records (30 Non-Diabetic, 8 Pre-Diabetic, 212 Diabetic)

### 📋 Detailed Classification Report

| Diagnostic Category | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Non-Diabetic (N)** | 0.97 | 0.93 | 0.95 | 30 |
| **Pre-Diabetic (P)** | 0.89 | 1.00 | 0.94 | 8 |
| **Diabetic (Y)** | 0.99 | 0.99 | 0.99 | 212 |
| **Macro Average** | *0.95* | *0.97* | *0.96* | *250* |
| **Weighted Average** | **0.98** | **0.98** | **0.98** | **250** |

### 🧩 Confusion Matrix Analysis
```text
Actual \ Predicted   [N]   [P]   [Y]
   [N] (Healthy)      28     0     2
   [P] (Pre-Diabetic)  0     8     0
   [Y] (Diabetic)      1     1   210
```
### 🔍 Key Insights & Clinical Reliability
1. **Critical Sensitivity (Recall):** The model demonstrates an elite 99% Recall for the Diabetic class and a 100% Recall for the Pre-Diabetic class. In medical terms, this indicates an incredibly low false-negative rate, making it highly dependable for early screening.
2. **Precision Consistency:** With a 99% precision for positive diabetic flags, the system ensures that medical staff experience minimal false alarms.

---


