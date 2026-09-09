# 📊 Data Profiler

> **A practical, end-to-end Python data profiling and exploratory data analysis project**  
> Load data from multiple sources → inspect → profile → clean → visualize → discover relationships.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C78A8?style=for-the-badge)](https://seaborn.pydata.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

---

## 🚀 Overview

**Data Profiler** is a practical Python project designed to demonstrate the complete first-stage data analytics workflow.

The project works with customer data and covers:

- 📥 Loading data from **CSV**
- 🧾 Loading data from **JSON**
- 🗄️ Querying data from **SQLite**
- 🌐 Fetching records from a **REST API**
- 🔎 Understanding dataset structure and data types
- 🕳️ Detecting missing values
- ♻️ Detecting duplicate records
- 🧹 Cleaning customer data
- 📊 Univariate, bivariate and multivariate EDA
- 🔗 Correlation analysis
- 📈 Statistical summaries and visual exploration

The included practical notebook also installs **`ydata-profiling`**, making the project suitable for extending into automated exploratory data profiling.

---

## 🎯 Project Objectives

The main objective is to build a reusable foundation for data analysis by answering questions such as:

> **What does the dataset contain?**  
> **Is the data clean?**  
> **What values are missing?**  
> **Are duplicate records present?**  
> **How are variables distributed?**  
> **Which variables appear related?**

This project demonstrates how raw data can be transformed into an analysis-ready dataset through a structured workflow.

---

## 🧠 Data Analytics Workflow

```text
        ┌──────────────────────┐
        │     Data Sources     │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │       Ingestion      │
        │ CSV • JSON • SQLite  │
        │      • REST API      │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │   Data Understanding │
        │ Shape • Columns      │
        │ Types • Statistics   │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │      Data Quality    │
        │ Missing • Duplicates │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │      Data Cleaning   │
        │ Imputation • Dedup   │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │         EDA          │
        │ Uni • Bi • Multivar. │
        └──────────┬───────────┘
                   │
        ┌──────────▼───────────┐
        │   Insights & Ready   │
        │    for Analysis      │
        └──────────────────────┘
```

---

## 📁 Project Structure

```text
Data-Profiler/
│
├── 📓 Data_Profiler_Practicals.ipynb
├── 🐍 data_profiler.py
│
├── 📂 data/
│   ├── customers.csv
│   ├── customers.json
│   └── customers.db
│
├── 📄 README.md
└── 📄 requirements.txt
```

> **Note:** The repository can use either the `data/` structure shown above or the current flat-file layout. Update the notebook paths accordingly if the files are stored beside the notebook.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 🐼 Pandas | Data loading, transformation & analysis |
| 🔢 NumPy | Numerical operations |
| 📊 Matplotlib | Data visualization |
| 🎨 Seaborn | Statistical visualization |
| 🗄️ SQLite3 | Database connectivity |
| 🌐 Requests | REST API requests |
| 📓 Jupyter Notebook | Interactive analysis |
| 🔍 ydata-profiling | Automated data profiling extension |

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/data-profiler.git
cd data-profiler
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install pandas numpy matplotlib seaborn requests ydata-profiling jupyter
```

Or, if you create a `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Jupyter Notebook

```bash
jupyter notebook
```

Then open:

```text
Data_Profiler_Practicals.ipynb
```

### Python helper module

```bash
python data_profiler.py
```

---

# 📥 Data Ingestion

## 1. CSV Data

The project loads customer data using Pandas:

```python
df = pd.read_csv("customers.csv")
```

The sample customer dataset contains fields such as:

```text
CustomerID
Age
Gender
Income
Orders
Purchases
City
SignupDate
```

---

## 2. JSON Data

JSON records are loaded using:

```python
json_df = pd.read_json("customers.json")
```

This demonstrates how the same type of customer information can be consumed from a structured JSON source.

---

## 3. SQLite Database

The project connects to SQLite using Python's built-in `sqlite3` module:

```python
conn = sqlite3.connect("customers.db")

sql_df = pd.read_sql_query(
    "SELECT * FROM customers",
    conn
)

conn.close()
```

It also demonstrates filtering records directly with SQL:

```sql
SELECT CustomerID, Age, Gender, Income, Orders, Purchases
FROM customers
WHERE Income > 40000;
```

---

## 4. REST API

The notebook demonstrates API ingestion using `requests`:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=15)
response.raise_for_status()

api_data = response.json()
api_df = pd.DataFrame(api_data)
```

This introduces the concept of bringing external API data into a Pandas DataFrame for analysis.

---

# 🔍 Data Understanding

Before cleaning or modeling data, the project inspects its structure.

### Preview records

```python
df.head()
```

### Dataset dimensions

```python
df.shape
```

### Column names

```python
df.columns.tolist()
```

### Data types and non-null information

```python
df.info()
```

### Statistical summary

```python
df.describe(include="all")
```

### Data types

```python
df.dtypes
```

This stage provides an initial understanding of the dataset before applying transformations.

---

# 🕳️ Data Quality Analysis

## Missing Values

Missing values are identified column-by-column:

```python
df.isnull().sum()
```

Total missing values:

```python
df.isnull().sum().sum()
```

## Duplicate Records

Duplicate rows are checked using:

```python
df.duplicated().sum()
```

The supplied sample data intentionally contains missing values and a repeated customer record, making it useful for demonstrating data-quality handling.

---

# 🧹 Data Cleaning

The project performs simple, explainable data-cleaning operations.

### Numeric Imputation

Missing `Age` values are replaced with the column median:

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

Missing `Income` values are handled in the same way:

```python
df["Income"] = df["Income"].fillna(df["Income"].median())
```

### Categorical Imputation

Missing `Gender` values are filled using the most frequent category:

```python
df["Gender"] = df["Gender"].fillna(
    df["Gender"].mode()[0]
)
```

### Duplicate Removal

```python
df = df.drop_duplicates()
```

### Reusable Cleaning Function

The helper module provides a reusable function:

```python
def clean_customer_data(df):
    data = df.copy()

    if "Age" in data.columns:
        data["Age"] = data["Age"].fillna(data["Age"].median())

    if "Income" in data.columns:
        data["Income"] = data["Income"].fillna(
            data["Income"].median()
        )

    if "Gender" in data.columns:
        data["Gender"] = data["Gender"].fillna(
            data["Gender"].mode()[0]
        )

    data = data.drop_duplicates()

    return data
```

This keeps the original DataFrame untouched and returns a cleaned copy.

---

# 📊 Exploratory Data Analysis

The project performs three levels of EDA.

## 1️⃣ Univariate Analysis

Univariate analysis studies one variable at a time.

### 👤 Age Distribution

A histogram with KDE is used to understand the distribution of customer ages.

### 💰 Income Distribution

A histogram is used to examine income distribution.

### 🛒 Purchase Distribution

A histogram is used to explore customer purchase values.

Example:

```python
sns.histplot(clean_df["Age"], kde=True)
```

---

## 2️⃣ Bivariate Analysis

Bivariate analysis studies relationships between two variables.

### 👥 Gender vs Purchases

A boxplot compares purchase distributions across gender categories:

```python
sns.boxplot(
    data=clean_df,
    x="Gender",
    y="Purchases"
)
```

### 💰 Income vs Orders

A scatterplot examines the relationship between customer income and number of orders:

```python
sns.scatterplot(
    data=clean_df,
    x="Income",
    y="Orders"
)
```

---

## 3️⃣ Multivariate Analysis

Multivariate analysis explores multiple variables together.

### 🔥 Correlation Heatmap

Numeric columns are selected and their correlations are visualized:

```python
numeric_df = clean_df.select_dtypes(
    include="number"
)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f"
)
```

### 🔗 Pairplot

The project compares:

```text
Age
Income
Orders
Purchases
```

using:

```python
sns.pairplot(
    clean_df[
        ["Age", "Income", "Orders", "Purchases"]
    ]
)
```

---

# 🧩 Feature Handling

`CustomerID` is an identifier rather than an analytical measurement, so the notebook creates an analysis DataFrame without it:

```python
analysis_df = clean_df.drop(
    columns=["CustomerID"]
)
```

This separates identification fields from variables used for analytical exploration.

---

# 📋 Dataset Schema

| Column | Description | Example |
|---|---|---|
| `CustomerID` | Unique customer identifier | `C001` |
| `Age` | Customer age | `21` |
| `Gender` | Customer gender | `Male` |
| `Income` | Customer income | `25000` |
| `Orders` | Number of orders | `3` |
| `Purchases` | Purchase amount | `4500` |
| `City` | Customer city | `Indore` |
| `SignupDate` | Customer registration date | `2025-01-10` |

---

# 🔬 Automated Profiling — Next-Level Extension

The notebook installs:

```bash
pip install ydata-profiling
```

A natural next step is generating an automated profiling report:

```python
from ydata_profiling import ProfileReport

profile = ProfileReport(
    clean_df,
    title="Customer Data Profiling Report",
    explorative=True
)

profile.to_file("customer_profile.html")
```

This can provide a richer automated overview of data quality, distributions, correlations and variable-level statistics.

---

# 💡 Key Learning Outcomes

By completing this project, you practice:

- ✅ Multi-source data ingestion
- ✅ Pandas DataFrame operations
- ✅ SQL-based data extraction
- ✅ REST API data collection
- ✅ Data inspection
- ✅ Missing-value detection
- ✅ Duplicate detection
- ✅ Numeric and categorical imputation
- ✅ Exploratory Data Analysis
- ✅ Statistical visualization
- ✅ Correlation analysis
- ✅ Reusable Python functions
- ✅ Separation of identifiers from analysis variables
- ✅ Foundations of real-world data preprocessing

---

# 🏗️ Architecture

```text
                DATA PROFILER
                      │
       ┌──────────────┼──────────────┐
       │              │              │
      CSV            JSON          SQLite
       │              │              │
       └──────────────┼──────────────┘
                      │
                   REST API
                      │
                      ▼
              ┌───────────────┐
              │ Pandas Layer  │
              └───────┬───────┘
                      │
             ┌────────▼────────┐
             │ Data Inspection  │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │ Quality Checks   │
             │ Missing/Dupes    │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │ Data Cleaning    │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │      EDA         │
             │ Uni / Bi / Multi │
             └────────┬────────┘
                      │
             ┌────────▼────────┐
             │ Insights / Next  │
             │ Analytics Stage  │
             └─────────────────┘
```

---

# 🧪 Example Cleaning Flow

```python
import pandas as pd

df = pd.read_csv("customers.csv")

print("Before cleaning:")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

clean_df = df.copy()

clean_df["Age"] = clean_df["Age"].fillna(
    clean_df["Age"].median()
)

clean_df["Income"] = clean_df["Income"].fillna(
    clean_df["Income"].median()
)

clean_df["Gender"] = clean_df["Gender"].fillna(
    clean_df["Gender"].mode()[0]
)

clean_df = clean_df.drop_duplicates()

print("\nAfter cleaning:")
print(clean_df.isnull().sum())
print("Duplicates:", clean_df.duplicated().sum())
```

---

# 📈 Future Enhancements

This project can be upgraded into a more advanced **Data Quality & Profiling Platform**.

### 🔥 Potential Features

- [ ] Automated profiling dashboard
- [ ] Interactive Plotly charts
- [ ] Streamlit web application
- [ ] Automated data-quality score
- [ ] Outlier detection using IQR/Z-score
- [ ] Data-type inference
- [ ] Date parsing and validation
- [ ] Cardinality analysis
- [ ] Unique-value profiling
- [ ] Automated anomaly detection
- [ ] Export profiling reports to HTML/PDF
- [ ] Upload CSV/Excel/JSON from a UI
- [ ] Database connector support
- [ ] Data-quality alerts
- [ ] Automated cleaning recommendations
- [ ] Dataset comparison/versioning
- [ ] ML-ready preprocessing pipeline

---

# 🧑‍💻 Recommended GitHub Presentation

For a professional GitHub repository, showcase:

```text
⭐ Project title
│
├── 🚀 Overview
├── 🎯 Objectives
├── 🧠 Workflow
├── 🛠️ Tech Stack
├── 📁 Project Structure
├── 📥 Data Sources
├── 🔍 Data Profiling
├── 🧹 Data Cleaning
├── 📊 EDA
├── 🔥 Correlation Analysis
├── 📈 Visualizations
├── 💡 Learning Outcomes
├── 🏗️ Architecture
├── 🚀 Installation
├── ▶️ Usage
├── 🔬 Future Enhancements
└── 📜 License
```

---

# 👨‍💻 Author

**Indrajeet Maheshwari**

📊 Aspiring Data Analyst | Python | SQL | Power BI | Data Visualization

> If you found this project useful, consider giving the repository a ⭐

---

# ⭐ Support

If this project helped you understand data profiling and exploratory data analysis:

**⭐ Star the repository**  
**🍴 Fork the project**  
**💬 Share your feedback**

---

## 📜 License

This project is intended for educational and portfolio purposes. Add a specific open-source license such as **MIT** if you plan to distribute the project publicly.
