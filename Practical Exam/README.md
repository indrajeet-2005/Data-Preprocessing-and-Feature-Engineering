# 🚀 Data Preprocessing & Feature Engineering Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Preprocessing-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge" alt="Seaborn">
</p>

<p align="center">
  <b>🧹 Data Cleaning • 🔍 EDA • 🩹 Missing Value Treatment • 📊 Outlier Detection • 🔤 Encoding • ⚖️ Scaling • 🛠️ Feature Engineering</b>
</p>

---

## 👨‍💻 Author

**Indrajeet Maheshwari**

> A complete practical data-preprocessing notebook covering data import, exploration, cleaning, transformation, feature engineering, and final dataset preparation.

---

## 📌 Project Overview

This project demonstrates an end-to-end **Data Preprocessing and Feature Engineering workflow** using Python.

The notebook works with multiple data sources and combines them into a single customer transaction dataset. It then performs exploratory analysis, handles missing values, detects outliers, processes dates, encodes categorical variables, applies different scaling techniques, creates new features, transforms numerical data, and finally exports a processed CSV dataset.

### 🎯 Main Goal

The main objective is to transform raw, mixed-source data into a **clean, structured, feature-rich dataset** that can be used as a foundation for further analytics or machine-learning tasks.

---

## ✨ What This Project Covers

| # | Module | What is Performed |
|---|---|---|
| 1️⃣ | 📥 Data Import | Excel, JSON, SQL and API data |
| 2️⃣ | 🔗 Data Integration | Customer + transaction + product data |
| 3️⃣ | 🔍 EDA | Numerical, categorical and correlation analysis |
| 4️⃣ | 🩹 Missing Values | Analysis, median/mode imputation, KNN, MICE |
| 5️⃣ | 🚨 Outliers | Z-score, IQR, percentile method, Winsorization |
| 6️⃣ | 📅 Date/Time | Date conversion and date-derived features |
| 7️⃣ | 🔤 Encoding | Label, One-Hot and Ordinal Encoding |
| 8️⃣ | ⚖️ Scaling | Standard, Min-Max, MaxAbs, Robust and Normalizer |
| 9️⃣ | 🛠️ Feature Engineering | Aggregation, ratios, transformations and flags |
| 🔟 | 💾 Final Dataset | Validation and CSV export |

---

# 🗂️ Project Structure

```text
📦 Data Preprocessing Project
│
├── 📓 DataPreprocessing.ipynb
│
├── 📁 Dataset
│   ├── 📄 customers.xlsx
│   ├── 📄 transactions.json
│   └── 📄 products.sql
│
└── 📁 Final Dataset
    └── 📄 processed_customer_data.csv
```

> ℹ️ The notebook automatically looks for a `Dataset` folder and creates the `Final Dataset` folder when required.

---

# 🧰 Technologies & Libraries

### 🐍 Core Python Libraries

- 🐼 **Pandas** — DataFrames, data cleaning and manipulation
- 🔢 **NumPy** — Numerical operations and transformations
- 📊 **Matplotlib** — Data visualization
- 🎨 **Seaborn** — Statistical visualizations
- 🗄️ **SQLite3** — Reading and working with SQL data
- 🌐 **Requests** — API data retrieval
- 🧮 **SciPy** — Z-score, Winsorization and statistical operations
- 🤖 **Scikit-learn** — Imputation, encoding, scaling and transformations

### 📦 Important Scikit-learn Components

```text
KNNImputer
IterativeImputer
LabelEncoder
OrdinalEncoder
StandardScaler
MinMaxScaler
MaxAbsScaler
RobustScaler
Normalizer
PowerTransformer
ColumnTransformer
```

---

# 📥 1. Data Import & Understanding

The notebook demonstrates importing data from different formats.

### 👥 Customer Data

Customer information is loaded from:

```text
customers.xlsx
```

The notebook examines:

- Dataset preview
- Dataset shape
- Column names
- Customer attributes such as age, gender, city and income

A fallback sample DataFrame is also included if the Excel dependency raises an `ImportError`.

### 🧾 Transaction Data

Transaction records are loaded from:

```text
transactions.json
```

The JSON data is converted into a Pandas DataFrame.

### 🛍️ Product Data

Product information is loaded from:

```text
products.sql
```

The SQL script is executed inside an in-memory SQLite database and the `products` table is read into Pandas.

### 🌐 API Data

The notebook also demonstrates API integration using:

```text
https://dummyjson.com/users
```

The API response is converted into a DataFrame and customer/API IDs are checked for possible matching records.

---

# 🔗 2. Data Integration

The project combines datasets using Pandas `merge()`.

### Customer + Transactions

```python
customer_transactions = pd.merge(
    customers,
    transactions,
    on="customer_id",
    how="left"
)
```

### Customer Transactions + Products

```python
combined_data = pd.merge(
    customer_transactions,
    products,
    on="product_id",
    how="left"
)
```

This creates the main combined dataset used throughout the preprocessing pipeline.

---

# 🔍 3. Exploratory Data Analysis — EDA

The notebook performs multiple EDA operations to understand the dataset.

### 🔢 Numerical Analysis

Numerical columns are detected automatically and visualized using histograms.

### 🔤 Categorical Analysis

Categorical columns are identified and their value frequencies are examined.

### 🔥 Correlation Analysis

A correlation heatmap is created for numerical variables.

### 📈 Relationship Analysis

The notebook visualizes:

- 💰 Income vs Purchase Amount
- 🛒 Purchase Amount by Product Category

### 📦 Duplicate Check

Duplicate rows are also checked using:

```python
combined_data.duplicated().sum()
```

---

# 🩹 4. Missing Data Analysis & Imputation

The project demonstrates several approaches to missing data.

## 🔎 Missing Value Analysis

The notebook calculates:

- Missing value count
- Missing value percentage
- Missing value summary
- Missing value heatmap

---

## 🧮 Median & Mode Imputation

Numerical variables:

```text
age
income
```

are filled using their median values.

Categorical variables:

```text
city
gender
```

are filled using their mode values.

---

## 🤖 KNN Imputation

`KNNImputer` is demonstrated using:

```text
age
income
amount
price
stock
```

with:

```python
KNNImputer(n_neighbors=3)
```

---

## 🔄 MICE / Iterative Imputation

The notebook also demonstrates iterative imputation using:

```python
IterativeImputer(
    max_iter=10,
    random_state=42
)
```

---

## 🗑️ Complete Case Analysis

Rows containing missing values are removed using:

```python
combined_data.dropna()
```

The notebook compares the number of remaining rows with the number of removed rows.

---

# 🚨 5. Outlier Detection

Multiple outlier-detection techniques are included.

### 📐 Z-Score Method

The notebook calculates absolute Z-scores and identifies rows where:

```text
Z-score > 3
```

---

### 📦 IQR Method

The Interquartile Range method calculates:

```text
Q1
Q3
IQR = Q3 - Q1
```

and uses:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

---

### 📊 Percentile Method

The notebook uses:

```text
1st percentile
99th percentile
```

as boundaries for identifying extreme values.

---

### ✂️ Winsorization

Winsorization is demonstrated with:

```python
limits=[0.05, 0.05]
```

This caps extreme values at the selected lower and upper limits.

---

# 📅 6. Date/Time & Mixed Variables

The transaction date is converted into a proper Pandas datetime format.

```python
combined_data["date"] = pd.to_datetime(combined_data["date"])
```

### ⏳ Days Since Last Purchase

A reference date is taken from the maximum transaction date.

A new feature is then created:

```text
days_since_last_purchase
```

### 📆 Calendar Features

The project extracts:

- 📅 Purchase Year
- 🗓️ Purchase Month
- 📌 Purchase Day of Week

---

# 🔤 7. Categorical Encoding

Several categorical encoding methods are demonstrated.

## 🏷️ Label Encoding

Gender is converted into numeric values using `LabelEncoder`.

```text
gender
   ↓
gender_encoded
```

The notebook also prints the encoding mapping.

---

## 🧩 One-Hot Encoding

The following categorical columns are one-hot encoded:

```text
city
payment_mode
```

Later, the final dataset also one-hot encodes:

```text
city
payment_mode
category
product_name
```

---

## 🔢 Ordinal Encoding

An ordered satisfaction example is demonstrated:

```text
Low → Medium → High
```

Income groups are also created and encoded in this order:

```text
Low → Medium → High
```

---

# ⚖️ 8. Feature Scaling

The notebook compares multiple scaling techniques.

### 📏 StandardScaler

Standardizes numerical variables.

### 🔽 MinMaxScaler

Scales values using the minimum and maximum values.

### ➕ MaxAbsScaler

Scales according to the maximum absolute value.

### 🛡️ RobustScaler

Uses statistics that are more resistant to extreme values.

### 📐 Normalizer

Normalizes rows based on their vector norm.

---

## 🧩 ColumnTransformer

The project also demonstrates applying different transformations to different columns:

```text
age, income
    ↓
StandardScaler

amount, price, stock
    ↓
MinMaxScaler
```

This shows how different feature groups can receive different preprocessing techniques.

---

# 🛠️ 9. Feature Construction & Transformation

The notebook creates several engineered features.

## 🧮 Total Purchases

The number of transactions per customer is calculated:

```text
total_purchases
```

---

## 💰 Amount Per Purchase

A ratio is created:

```text
amount_per_purchase
```

---

## 📈 Mathematical Transformations

The project demonstrates:

- `log1p()` → Log transformation
- `sqrt()` → Square-root transformation
- Reciprocal transformation
- Box-Cox transformation
- Yeo-Johnson transformation

### 🔄 Example

```python
feature_data["log_amount"] = np.log1p(
    feature_data["amount"]
)
```

---

## 💼 Income Group

Income is divided into:

```text
0 – 50,000       → Low
50,000 – 70,000  → Medium
70,000+          → High
```

---

## 🛒 Frequent Buyer Feature

A binary feature is created:

```text
frequent_buyer
```

The current notebook uses a purchase threshold of `1`.

---

# 💾 10. Final Processed Dataset

The final processing stage combines the engineered features and prepares the final feature matrix.

### Final processing includes:

```text
✅ Label Encoding
✅ Ordinal Encoding
✅ One-Hot Encoding
✅ Standard Scaling
✅ Removing selected raw/text identifier fields
✅ Keeping customer_id as an identifier
✅ Sorting by customer_id
```

The final dataset removes selected fields that are not intended to be used as model features:

```text
name
transaction_id
product_id
date
gender
income_group
```

The processed dataset is sorted by:

```text
customer_id
```

---

# 📤 Output

The processed dataset is exported as:

```text
Final Dataset/processed_customer_data.csv
```

The notebook also performs final validation by checking:

- 📋 Final columns
- ❌ Missing values
- 📐 Final dataset information
- 🧪 Processed dataset shape

---

# 🔄 Complete Workflow

```text
                📥 RAW DATA
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Excel 📊      JSON 📄      SQL 🗄️
       │            │            │
       └────────────┼────────────┘
                    ▼
              🌐 API Check
                    │
                    ▼
             🔗 DATA MERGING
                    │
                    ▼
             🔍 EDA / ANALYSIS
                    │
                    ▼
          🩹 MISSING VALUE HANDLING
                    │
                    ▼
            🚨 OUTLIER DETECTION
                    │
                    ▼
              📅 DATE FEATURES
                    │
                    ▼
             🔤 ENCODING
                    │
                    ▼
               ⚖️ SCALING
                    │
                    ▼
          🛠️ FEATURE ENGINEERING
                    │
                    ▼
           🧪 FINAL VALIDATION
                    │
                    ▼
             💾 CSV EXPORT
                    │
                    ▼
       📄 processed_customer_data.csv
```

---

# ⚙️ Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn openpyxl requests
```

> 💡 `openpyxl` is useful for reading the Excel input file used by the notebook.

---

# ▶️ How to Run

### 1️⃣ Clone or download the project

Place the notebook and `Dataset` folder in the same project directory.

### 2️⃣ Check the folder structure

Make sure the following files are available:

```text
Dataset/
├── customers.xlsx
├── transactions.json
└── products.sql
```

### 3️⃣ Open the notebook

Open:

```text
DataPreprocessing.ipynb
```

using Jupyter Notebook, JupyterLab, VS Code, or another compatible notebook environment.

### 4️⃣ Run the cells

Run the notebook from top to bottom so that the datasets and intermediate variables are created in the correct order.

### 5️⃣ Check the output

After successful execution, the notebook saves:

```text
Final Dataset/processed_customer_data.csv
```

---

# 📊 Preprocessing Techniques Summary

| Technique | Purpose |
|---|---|
| 📥 Data Import | Load data from different sources |
| 🔗 Merge | Combine related datasets |
| 🔍 EDA | Understand data structure and patterns |
| 🩹 Median/Mode | Basic missing-value treatment |
| 🤖 KNN Imputer | Neighbor-based numerical imputation |
| 🔄 Iterative Imputer | Iterative missing-value estimation |
| 📐 Z-Score | Detect statistical outliers |
| 📦 IQR | Detect distribution-based outliers |
| 📊 Percentile | Detect extreme values |
| ✂️ Winsorization | Limit extreme observations |
| 🏷️ Label Encoding | Convert labels to numeric values |
| 🧩 One-Hot Encoding | Convert nominal categories to binary columns |
| 🔢 Ordinal Encoding | Preserve category order |
| ⚖️ Scaling | Put numerical features on comparable scales |
| 🛠️ Feature Engineering | Create useful derived variables |
| 🔄 Power Transform | Transform numerical distributions |
| 💾 CSV Export | Save the final processed dataset |

---

# 🎓 Learning Outcomes

After completing this notebook, you can understand how to:

- 📥 Import data from Excel, JSON, SQL and APIs
- 🔗 Combine multiple datasets
- 🔍 Perform basic exploratory data analysis
- 🩹 Identify and handle missing values
- 🤖 Apply KNN and iterative imputation
- 🚨 Detect outliers using different approaches
- 📅 Extract useful information from dates
- 🔤 Encode categorical variables
- ⚖️ Compare different feature-scaling methods
- 🛠️ Create new analytical features
- 🔄 Apply mathematical and power transformations
- 💾 Prepare and export a processed dataset

---

# 🧠 Key Concepts Demonstrated

```text
Data Understanding
       ↓
Data Integration
       ↓
Exploratory Data Analysis
       ↓
Data Cleaning
       ↓
Missing Value Treatment
       ↓
Outlier Detection
       ↓
Feature Transformation
       ↓
Categorical Encoding
       ↓
Feature Scaling
       ↓
Feature Engineering
       ↓
Final Dataset Preparation
```

---

# 🏁 Final Result

The notebook produces a processed customer dataset containing engineered and transformed features suitable as a **preprocessing foundation for downstream analytics or machine-learning workflows**.

The final exported file is:

```text
📄 processed_customer_data.csv
```

---

## 👨‍💻 Author

### **Indrajeet Maheshwari**

📌 **Project:** Data Preprocessing & Feature Engineering  
🐍 **Language:** Python  
📓 **Notebook:** DataPreprocessing.ipynb

---

<p align="center">
  <b>⭐ If you found this project useful, consider giving it a star!</b>
</p>

<p align="center">
  Made with ❤️ using Python, Pandas, NumPy & Scikit-learn
</p>
