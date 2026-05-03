# 🤖 AI Job Market Data Analysis

A professional data analysis project exploring the **AI Job Market Dataset** as part of the Code Alpha Data Science Internship.
This project covers Exploratory Data Analysis (EDA) and Data Visualization to uncover meaningful insights about salaries, job demand, and hiring trends in the AI industry.

---

## 📁 Project Structure

```
Code_Alpha_Tasks/
│
├── data/
│   └── AI Job Market Dataset.csv       # Raw dataset
│
├── scripts/
│   ├── task_2_eda.py                   # Task 2: Exploratory Data Analysis
│   └── task_3_data_visualization.py    # Task 3: Data Visualization
│
├── outputs/
│   ├── reports/
│   │   └── task_2_eda_report.md        # Auto-generated EDA report
│   └── visualizations/
│       ├── 1_salary_distribution.png
│       ├── 2_salary_by_experience.png
│       ├── 3_salary_by_remote_type.png
│       ├── 4_correlation_heatmap.png
│       └── 5_top_industries_job_openings.png
│
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

---

## 📋 Tasks

### Task 2: Exploratory Data Analysis (EDA)
**Script:** `scripts/task_2_eda.py`

- ❓ Asks meaningful questions about the dataset before analysis
- 🔍 Explores data structure including variables and data types
- 📈 Identifies trends, patterns, and anomalies within the data
- 🧪 Tests hypotheses using statistical methods (T-test, Pearson Correlation)
- ⚠️ Detects potential data issues such as outliers and missing values

**Output:** `outputs/reports/task_2_eda_report.md`

---

### Task 3: Data Visualization
**Script:** `scripts/task_3_data_visualization.py`

Generates 5 high-quality charts using `matplotlib` and `seaborn`:

| # | Chart | Insight |
|---|-------|---------|
| 1 | Salary Distribution (Histogram + KDE) | Overall salary spread in AI roles |
| 2 | Average Salary by Experience Level | How seniority affects pay |
| 3 | Salary by Remote Type (Violin Plot) | Remote vs Hybrid vs Onsite pay comparison |
| 4 | Correlation Heatmap | Relationships between numerical features |
| 5 | Top 10 Industries by Job Openings | Where AI hiring is most active |

**Output:** `outputs/visualizations/`

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the EDA Script
```bash
python scripts/task_2_eda.py
```

### 3. Run the Visualization Script
```bash
python scripts/task_3_data_visualization.py
```

---

## 📦 Dataset

**File:** `data/AI Job Market Dataset.csv`
- **Rows:** 10,345
- **Columns:** 19
- **Key Features:** `job_title`, `salary`, `experience_level`, `remote_type`, `company_industry`, `years_experience`, `skills_*`

---

## 🔑 Key Findings

- 💰 **Salary** ranges widely across roles, with a few outliers detected via the IQR method.
- 📊 **Experience level** is a strong predictor of salary — Senior roles earn significantly more.
- 🌍 **Remote vs Onsite** salary differences were found to be statistically insignificant (p > 0.05).
- 🏭 **Technology** and **Finance** industries show the highest AI job demand.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `scipy` | Statistical hypothesis testing |
| `matplotlib` | Core plotting library |
| `seaborn` | Statistical data visualization |

---

