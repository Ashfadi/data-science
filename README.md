# Census Data Analysis

## Overview
This project analyzes U.S. Census data to uncover patterns related to income, education, professions, and age distribution. The analysis includes data cleaning, exploration, visualization, and key insights. The goal is to provide actionable insights through visualizations and statistical exploration.

## Objectives
- Clean and preprocess raw census data for meaningful analysis.
- Explore demographic and income patterns based on age, gender, and education.
- Visualize the data to make findings intuitive and easy to understand.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib
- **Tools**: Jupyter Notebook

## Steps
1. **Data Cleaning**:
   - Standardized categorical variables (e.g., combining similar work classes into unified categories like "Government" and "Self-employed").
   - Removed rows with missing or invalid data.
   - Discretized income into two groups: `<=50K` and `>50K`.

2. **Data Analysis**:
   - Examined income distribution and demographic trends.
   - Grouped data by age, gender, and education for deeper insights.
   - Compared cleaned data with a sample dataset for validation.

3. **Visualizations**:
   - Histograms for age distribution.
   - Pie charts for profession distribution across age groups.
   - Bar charts to compare education levels by gender and age groups.

## Key Findings
- **Income Trends**: 
  - Individuals aged 41-60 dominate the `>50K` income group.
- **Profession Distribution**: 
  - Private employment is the largest sector across all age groups, while self-employment increases with age.
- **Education and Gender**:
  - Males hold a higher percentage of advanced degrees (Masters, Doctorates) compared to females, particularly in older age groups.

---

## Visualizations

### 1. Age Distribution (Cleaned Data)
![Age Distribution (Cleaned Data)](images/Histogram_cd.png)

### 2. Age Distribution (Sample Data)
![Age Distribution (Sample Data)](images/Histogram_sd.png)

### 3. Profession Distribution by Age Groups (Cleaned Data)
![Profession Distribution (Cleaned Data)](images/PieChart_cd.png)

### 4. Profession Distribution by Age Groups (Sample Data)
![Profession Distribution (Sample Data)](images/PieChart_sd.png)

### 5. Education Comparison by Gender (Cleaned Data)
![Education Comparison (Cleaned Data)](images/barchart_cd.png)

### 6. Education Comparison by Gender (Sample Data)
![Education Comparison (Sample Data)](images/barchart_sd.png)

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Census-Data-Analysis.git
