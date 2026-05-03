import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# STEP 1: LOAD DATA & SETUP
# ─────────────────────────────────────────────
print("=" * 60)
print("SETUP & LOAD DATA")
print("=" * 60)

dataset_path = r"C:\Users\datas\Documents\projects\Code_Alpha_Tasks\data\AI Job Market Dataset.csv"
output_dir = r"C:\Users\datas\Documents\projects\Code_Alpha_Tasks\outputs\visualizations"

# Note: This assumes the "visualizations" folder already exists.
df = pd.read_csv(dataset_path)

# Set global plotting style
sns.set_theme(style="whitegrid")

print(f"Data loaded from AI Job Market Dataset.csv")
print(f"Visualizations will be saved to '{output_dir}/'")

# ─────────────────────────────────────────────
# STEP 2: SALARY DISTRIBUTION
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("GENERATING CHART: SALARY DISTRIBUTION")
print("=" * 60)

plt.figure(figsize=(10, 6))
sns.histplot(df['salary'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Salary Distribution for AI Roles')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()

file_name = '1_salary_distribution.png'
plt.savefig(f"{output_dir}/{file_name}", dpi=300)
plt.close()
print(f"\n {file_name}")

# ─────────────────────────────────────────────
# STEP 3: AVERAGE SALARY BY EXPERIENCE LEVEL
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("GENERATING CHART: AVERAGE SALARY BY EXPERIENCE")
print("=" * 60)

plt.figure(figsize=(10, 6))
order = ['Entry', 'Mid', 'Senior', 'Executive']
order = [lvl for lvl in order if lvl in df['experience_level'].unique()]

sns.barplot(x='experience_level', y='salary', data=df, order=order, hue='experience_level', legend=False, palette='viridis', errorbar=None)
plt.title('Average Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary')
plt.tight_layout()

file_name = '2_salary_by_experience.png'
plt.savefig(f"{output_dir}/{file_name}", dpi=300)
plt.close()
print(f"\n{file_name}")

# ─────────────────────────────────────────────
# STEP 4: SALARY VS REMOTE TYPE
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("GENERATING CHART: SALARY BY REMOTE TYPE")
print("=" * 60)

plt.figure(figsize=(10, 6))
sns.violinplot(x='remote_type', y='salary', data=df, hue='remote_type', legend=False, palette='Set2')
plt.title('Salary Distribution by Remote Type')
plt.xlabel('Remote Type')
plt.ylabel('Salary')
plt.tight_layout()

file_name = '3_salary_by_remote_type.png'
plt.savefig(f"{output_dir}/{file_name}", dpi=300)
plt.close()
print(f"\n {file_name}")

# ─────────────────────────────────────────────
# STEP 5: CORRELATION HEATMAP
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("GENERATING CHART: CORRELATION HEATMAP")
print("=" * 60)

plt.figure(figsize=(12, 8))
numeric_cols = df.select_dtypes(include=['number']).columns
corr_matrix = df[numeric_cols].corr()

sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()

file_name = '4_correlation_heatmap.png'
plt.savefig(f"{output_dir}/{file_name}", dpi=300)
plt.close()
print(f"\n{file_name}")

# ─────────────────────────────────────────────
# STEP 6: TOP INDUSTRIES BY JOB OPENINGS
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("GENERATING CHART: TOP INDUSTRIES BY JOB OPENINGS")
print("=" * 60)

plt.figure(figsize=(12, 6))
industry_counts = df.groupby('company_industry')['job_openings'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=industry_counts.values, y=industry_counts.index, hue=industry_counts.index, legend=False, palette='magma')
plt.title('Top 10 Industries by Total Job Openings')
plt.xlabel('Total Job Openings')
plt.ylabel('Industry')
plt.tight_layout()

file_name = '5_top_industries_job_openings.png'
plt.savefig(f"{output_dir}/{file_name}", dpi=300)
plt.close()
print(f"\n{file_name}")

print("\n" + "=" * 60)
print(f"ALL VISUALIZATIONS SAVED SUCCESSFULLY TO '{output_dir}/'")
print("=" * 60)
