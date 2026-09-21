# 🧹 Data Cleanser — Data Preprocessing & Outlier Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Scikit--learn-Imputation-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/SciPy-Statistics-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>

## 📌 Project Overview

**Data Cleanser** is a practical Python data-preprocessing project focused on cleaning a patient health-record dataset and preparing it for further analysis or machine-learning workflows.

The notebook demonstrates multiple techniques for:

- 🔎 Inspecting a dataset
- 🧩 Detecting and reporting missing values
- 🛠️ Treating missing numerical and categorical values
- 🎲 Using random-sample imputation with missing indicators
- 🤖 Applying KNN and MICE/Iterative imputation
- 🚨 Detecting potential outliers
- 📊 Comparing Z-Score, IQR and percentile methods
- ✂️ Applying Winsorization
- ✅ Creating a final cleaned dataset
- 💾 Saving the processed result

---

## 🎯 Aim

> To practice **data preprocessing and feature engineering** with a strong emphasis on **handling missing values and outlier detection/removal**.

---

## 📂 Dataset Information

The notebook works with a patient health-record dataset containing **1,200 rows and 9 columns**.

### 🧾 Features

| 🔢 Column | 📋 Description |
|---|---|
| `patient_id` | Unique patient identifier |
| `age` | Patient age |
| `gender` | Patient gender |
| `region` | Patient region |
| `bmi` | Body Mass Index |
| `blood_pressure` | Blood pressure value |
| `cholesterol` | Cholesterol level |
| `glucose` | Glucose level |
| `disease_risk` | Disease-risk target indicator |

---

## 🔍 Project Workflow

```text
📥 Load Dataset
      ↓
🔎 Initial Inspection
      ↓
🧩 Missing Value Report
      ↓
🛠️ Missing Value Treatment
      ├── Mean Imputation
      ├── Median Imputation
      ├── Most Frequent Imputation
      ├── Random Sample Imputation
      ├── KNN Imputation
      └── MICE Imputation
      ↓
🚨 Outlier Analysis
      ├── Z-Score
      ├── IQR
      ├── Percentile Method
      └── Winsorization
      ↓
🧹 Final Dataset
      ↓
✅ Final Validation
      ↓
💾 Save Result
```

---

## 🧩 Missing Value Treatment

The project explores several approaches instead of relying on a single technique.

### 1️⃣ Mean Imputation
Missing numerical values are replaced with the **mean** of the corresponding column.

### 2️⃣ Median Imputation
Missing numerical values are replaced with the **median**, providing an alternative to mean-based filling.

### 3️⃣ Most Frequent Imputation
Categorical missing values such as `gender` and `region` are filled using the **most frequent value**.

### 4️⃣ Random Sample Imputation 🎲
Missing numerical values are filled using randomly selected observed values from the same feature. A **missing indicator** is also created for the numerical columns.

### 5️⃣ KNN Imputation 🤖
`KNNImputer` is used with **5 neighbors** to estimate missing numerical values.

### 6️⃣ MICE / Iterative Imputation 🔄
`IterativeImputer` is used with **10 iterations** and a fixed random state for reproducibility.

---

## 🚨 Outlier Analysis

The project checks potential outliers in:

- `bmi`
- `blood_pressure`
- `cholesterol`
- `glucose`

### 📐 Methods Used

| Method | Purpose |
|---|---|
| 📏 **Z-Score** | Identifies values whose absolute Z-score is greater than 3 |
| 📦 **IQR** | Uses Q1, Q3 and the 1.5 × IQR rule |
| 📊 **Percentile Method** | Checks values outside the 1st and 99th percentiles |
| ✂️ **Winsorization** | Limits extreme values using 1% lower and upper limits |

---

## 📊 Initial Missing-Value Findings

Before cleaning, the notebook reports missing values in several columns:

| Column | Missing | Percentage |
|---|---:|---:|
| `patient_id` | 0 | 0% |
| `age` | 72 | 6% |
| `gender` | 48 | 4% |
| `region` | 60 | 5% |
| `bmi` | 84 | 7% |
| `blood_pressure` | 0 | 0% |
| `cholesterol` | 72 | 6% |
| `glucose` | 84 | 7% |
| `disease_risk` | 0 | 0% |

---

## 📈 Outlier Results

The notebook compares different outlier-detection techniques.

### Z-Score
- `bmi` → 5 potential outliers
- `blood_pressure` → 5 potential outliers
- `cholesterol` → 5 potential outliers
- `glucose` → 5 potential outliers

### IQR
- `bmi` → 7 potential outliers
- `blood_pressure` → 7 potential outliers
- `cholesterol` → 13 potential outliers
- `glucose` → 11 potential outliers

### Percentile Method
- `bmi` → 24 potential outliers
- `blood_pressure` → 24 potential outliers
- `cholesterol` → 24 potential outliers
- `glucose` → 12 potential outliers

> 💡 Different methods can identify different numbers of potential outliers because each method uses a different statistical rule.

---

## 🧹 Final Cleaning Strategy

For the final dataset, the notebook uses:

- 🔢 **Median imputation** for numerical columns
- 🏷️ **Most-frequent imputation** for categorical columns
- ✂️ **1% Winsorization** on selected numerical outlier columns

### ✅ Final Check

After cleaning, the notebook reports:

- **Missing values:** 0 across all columns
- **Final shape:** `1200 × 9`

---

## 🛠️ Technologies & Libraries

```text
🐍 Python
🐼 Pandas
🔢 NumPy
🤖 Scikit-learn
📐 SciPy
📊 Matplotlib
📓 Jupyter Notebook
```

### Main Libraries

- `pandas`
- `numpy`
- `scikit-learn`
- `scipy`
- `matplotlib`

---

## 🚀 How to Run

### 1️⃣ Clone or download the project

Make sure the notebook and dataset are available in the expected project structure.

### 2️⃣ Install dependencies

```bash
pip install pandas numpy scikit-learn scipy matplotlib
```

### 3️⃣ Open the notebook

```bash
jupyter notebook Data_Cleanser_Practical.ipynb
```

### 4️⃣ Run the cells ▶️

Run the notebook cells from top to bottom to reproduce the preprocessing and outlier-analysis workflow.

---

## 📁 Expected Project Structure

```text
📦 Data-Cleanser
 ┣ 📓 Data_Cleanser_Practical.ipynb
 ┣ 📂 data
 ┃ ┗ 📄 patient_health_records.csv
 ┗ 📄 README.md
```

---

## 💡 Key Learning Outcomes

By completing this project, you can understand:

- 🧠 Why data preprocessing is important
- 🔎 How to inspect raw datasets
- 🧩 How missing values are identified
- 🛠️ Different missing-value imputation techniques
- 🚨 How statistical methods detect potential outliers
- 📊 Why different outlier methods can produce different results
- ✂️ How Winsorization can limit extreme observations
- ✅ How to validate a cleaned dataset

---

## 👨‍💻 Author

### **Indrajeet Maheshwari**

📊 Data Analytics | 🐍 Python | 🗄️ SQL | 📈 Power BI

---

<p align="center">

### ⭐ Data Cleanser — Practical Data Preprocessing Project

**Made with 🐍 Python & ❤️ by Indrajeet Maheshwari**

</p>
