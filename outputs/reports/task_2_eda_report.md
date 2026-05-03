# Task 2: Exploratory Data Analysis (EDA) Report

## 1. Meaningful Questions
- How does salary vary across different experience levels?
- Is there a significant difference in salary between Remote and Onsite jobs?
- What is the correlation between years of experience and salary?
- Which industries have the highest demand (job openings) for AI roles?

## 2. Data Structure
### Basic Information
- **Total Rows:** 10345
- **Total Columns:** 19

### Columns and Data Types
- `job_id`: int64
- `job_title`: str
- `company_size`: str
- `company_industry`: str
- `country`: str
- `remote_type`: str
- `experience_level`: str
- `years_experience`: int64
- `education_level`: str
- `skills_python`: int64
- `skills_sql`: int64
- `skills_ml`: int64
- `skills_deep_learning`: int64
- `skills_cloud`: int64
- `salary`: int64
- `job_posting_month`: int64
- `job_posting_year`: int64
- `hiring_urgency`: str
- `job_openings`: int64

### Missing Values
- No missing values found in the dataset.

## 3. Trends, Patterns, and Anomalies
### Summary Statistics (Numerical)
```
         job_id  years_experience  skills_python  skills_sql  skills_ml  skills_deep_learning  skills_cloud     salary  job_posting_month  job_posting_year  job_openings
count  10345.00          10345.00       10345.00     10345.0   10345.00               10345.0      10345.00   10345.00           10345.00           10345.0      10345.00
mean    5173.00              6.95           0.49         0.5       0.51                   0.5          0.51  113438.23               6.50            2023.0          5.00
std     2986.49              4.32           0.50         0.5       0.50                   0.5          0.50   31389.20               3.47               2.0          2.58
min        1.00              0.00           0.00         0.0       0.00                   0.0          0.00   45083.00               1.00            2020.0          1.00
25%     2587.00              3.00           0.00         0.0       0.00                   0.0          0.00   89715.00               4.00            2021.0          3.00
50%     5173.00              7.00           0.00         1.0       1.00                   0.0          1.00  113082.00               6.00            2023.0          5.00
75%     7759.00             11.00           1.00         1.0       1.00                   1.0          1.00  134894.00              10.00            2025.0          7.00
max    10345.00             14.00           1.00         1.0       1.00                   1.0          1.00  204143.00              12.00            2026.0          9.00
```

### Anomalies
- Found **4** outliers in the `salary` column based on IQR method.

## 4. Hypothesis Testing and Assumptions
### Hypothesis 1: Salary Difference by Remote Type (Remote vs Onsite)
- **T-statistic:** -0.4601
- **P-value:** 0.6454
- **Conclusion:** There is no statistically significant difference in salaries between Remote and Onsite roles.

### Hypothesis 2: Correlation between Years of Experience and Salary
- **Pearson Correlation Coefficient:** -0.0133
- **P-value:** 1.7728e-01
- **Conclusion:** There is no statistically significant correlation between years of experience and salary.

## 5. Potential Data Issues for Further Analysis
- Outliers in salary might skew regression models. Consider capping or using robust models.