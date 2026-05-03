import pandas as pd
import numpy as np
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# STEP 1: LOAD DATA
# ─────────────────────────────────────────────
df = pd.read_csv(r"C:\Users\datas\Documents\projects\Code_Alpha_Tasks\data\AI Job Market Dataset.csv")
report_path = r"C:\Users\datas\Documents\projects\Code_Alpha_Tasks\outputs\reports\task_2_eda_report.md"
report_lines = []

report_lines.append("# Task 2: Exploratory Data Analysis (EDA) Report")
report_lines.append("\n## 1. Meaningful Questions")
report_lines.append("- How does salary vary across different experience levels?")
report_lines.append("- Is there a significant difference in salary between Remote and Onsite jobs?")
report_lines.append("- What is the correlation between years of experience and salary?")
report_lines.append("- Which industries have the highest demand (job openings) for AI roles?")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
print(df.head())

report_lines.append("\n## 2. Data Structure")
report_lines.append("### Basic Information")
report_lines.append(f"- **Total Rows:** {df.shape[0]}")
report_lines.append(f"- **Total Columns:** {df.shape[1]}")
report_lines.append("\n### Columns and Data Types")
for column in df.columns:
    report_lines.append(f"- `{column}`: {df[column].dtype}")

# ─────────────────────────────────────────────
# STEP 2: MISSING VALUES ANALYSIS
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()
report_lines.append("\n### Missing Values")

if missing.sum() == 0:
    print("No missing values found.")
    report_lines.append("- No missing values found in the dataset.")
else:
    for column in df.columns:
        if missing[column] > 0:
            print(f"  {column}: {missing[column]} missing values")
            report_lines.append(f"- `{column}`: {missing[column]} missing values")

# ─────────────────────────────────────────────
# STEP 3: BASIC STATISTICS
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

summary = df.describe().round(2)
print(summary)

report_lines.append("\n## 3. Trends, Patterns, and Anomalies")
report_lines.append("### Summary Statistics (Numerical)")
report_lines.append("```\n" + summary.to_string() + "\n```")

# ─────────────────────────────────────────────
# STEP 4: OUTLIER DETECTION (IQR Method)
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("OUTLIER DETECTION (IQR Method)")
print("=" * 60)

Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['salary'] < lower) | (df['salary'] > upper)]

print(f"  salary: {len(outliers)} outliers | Range [{lower:.1f}, {upper:.1f}]")

report_lines.append("\n### Anomalies")
report_lines.append(f"- Found **{len(outliers)}** outliers in the `salary` column based on IQR method.")

# ─────────────────────────────────────────────
# STEP 5: HYPOTHESIS TESTING
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("HYPOTHESIS TESTING")
print("=" * 60)

report_lines.append("\n## 4. Hypothesis Testing and Assumptions")

# Remote vs Onsite
print("\n[Hypothesis 1] Salary Difference by Remote Type (Remote vs Onsite)")
report_lines.append("### Hypothesis 1: Salary Difference by Remote Type (Remote vs Onsite)")

remote = df[df['remote_type'] == 'Remote']['salary'].dropna()
onsite = df[df['remote_type'] == 'Onsite']['salary'].dropna()

if len(remote) > 0 and len(onsite) > 0:
    t_stat, p_val = stats.ttest_ind(remote, onsite, equal_var=False)
    
    print(f"  T-statistic: {t_stat:.4f} | P-value: {p_val:.4f}")
    report_lines.append(f"- **T-statistic:** {t_stat:.4f}")
    report_lines.append(f"- **P-value:** {p_val:.4f}")

    if p_val < 0.05:
        print("  Conclusion: Statistically significant difference in salaries.")
        report_lines.append("- **Conclusion:** There is a statistically significant difference in salaries between Remote and Onsite roles.")
    else:
        print("  Conclusion: No statistically significant difference in salaries.")
        report_lines.append("- **Conclusion:** There is no statistically significant difference in salaries between Remote and Onsite roles.")
else:
    print("  Not enough data to compare Remote and Onsite salaries.")
    report_lines.append("- Not enough data to compare Remote and Onsite salaries.")

# Experience vs Salary
print("\n[Hypothesis 2] Correlation between Years of Experience and Salary")
report_lines.append("\n### Hypothesis 2: Correlation between Years of Experience and Salary")

data = df[['years_experience', 'salary']].dropna()

if len(data) > 1:
    corr, p_val = stats.pearsonr(data['years_experience'], data['salary'])
    
    print(f"  Pearson Correlation: {corr:.4f} | P-value: {p_val:.4e}")
    report_lines.append(f"- **Pearson Correlation Coefficient:** {corr:.4f}")
    report_lines.append(f"- **P-value:** {p_val:.4e}")

    if p_val < 0.05:
        print("  Conclusion: Statistically significant correlation between years of experience and salary.")
        report_lines.append("- **Conclusion:** There is a statistically significant correlation between years of experience and salary.")
    else:
        print("  Conclusion: No statistically significant correlation.")
        report_lines.append("- **Conclusion:** There is no statistically significant correlation between years of experience and salary.")

# ─────────────────────────────────────────────
# STEP 6: DATA ISSUES & REPORT GENERATION
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("POTENTIAL DATA ISSUES")
print("=" * 60)

report_lines.append("\n## 5. Potential Data Issues for Further Analysis")
issues = []

if missing.sum() > 0:
    issues.append("- Missing values need to be imputed or dropped.")
if len(outliers) > 0:
    issues.append("- Outliers in salary might skew regression models. Consider capping or using robust models.")
if (df['years_experience'] < 0).any():
    issues.append("- Found negative values in `years_experience`.")

if len(issues) == 0:
    print("  No major data issues detected. The dataset appears clean.")
    report_lines.append("- No major data issues detected. The dataset appears clean.")
else:
    for item in issues:
        print(f"  {item}")
        report_lines.append(item)

# Save report
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))

print("\nEDA successfully completed. Report generated at:", report_path)
