# Census Data Analysis

## Overview
This project focuses on analyzing U.S. Census data to uncover trends and insights about income, education levels, age distribution, and occupations. The data was cleaned, preprocessed, and visualized using Python libraries.

## Objectives
- Clean and preprocess raw census data for analysis.
- Explore demographic trends related to age, education, and income.
- Visualize key findings using plots and charts.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib
- **Tools**: Jupyter Notebook

## Key Steps
1. **Data Cleaning**: 
   - Standardized categorical values (e.g., combining similar categories like 'Federal-gov' and 'State-gov').
   - Removed missing or invalid data points.
2. **Data Preprocessing**:
   - Discretized gross income into ranges (`<=50K` and `>50K`).
   - Grouped ages into categories (e.g., `<21`, `21-40`, `41-60`, `>60`).
3. **Exploratory Data Analysis**:
   - Created frequency plots to analyze age distributions.
   - Generated pie charts to compare professions by age groups.
   - Grouped and compared education levels by gender.
   - Identified the top 5 occupations.
4. **Visualizations**:
   - Histograms for age distributions.
   - Pie charts for profession distribution.
   - Bar charts comparing education by gender.

## Visualizations
### Example: Frequency Plot for Age Groups
![Age Group Plot](images/age_groups.png)

### Example: Pie Chart for Profession Distribution
![Profession Distribution](images/professions.png)

## Results
- **Income Trends**: Majority of people earning `<=50K` were in specific age and education categories.
- **Education and Gender**: Higher education levels (Masters, Doctorate) were slightly more prevalent among males in older age groups.
- **Top 5 Occupations**:
  - Identified the most common occupations in the dataset.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ashfadi/Census-Data-Analysis.git
