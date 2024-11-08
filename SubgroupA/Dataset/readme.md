# ML Data Processing Workflow

Based on the data we collected from various sources, we first manually screened and removed irrelevant, redundant, and region-specific columns. In addition, the energy data was standardized by converting the total amount of each region or unit to a standard unit (e.g., kiloBTUs/sq. ft., kWh/sq. ft., BTUs/sq. ft.) to improve readability and comply with conversion factors.

## Data Preparation Steps

### Raw Data
The processed data is initially saved as `raw_data.xlsx`, where metric explanations are provided.

### Data Cleaning and Preprocessing
Data cleaning and preprocessing are performed through Python scripts as follows:

1. **Data Reading & Inspection**
   - Drop unnecessary columns such as "Order," "Property Id," "Parent Property Id," and "BBL - 10 digits" as they are irrelevant to the prediction task.
   - Convert columns with numerical values (e.g., ft²) into appropriate numerical data types.
   - Replace any logically impossible negative values in certain indicators with `NaN`.
   - Calculate missing values per column to understand data completeness.

2. **Exploratory Data Analysis (EDA)**
   - Analyze the dependent variable, applying a logarithmic transformation if needed.
   - Check for outliers using boxplots.
   - Process outliers by removing extreme values based on the IQR method.
   - Conduct variable analysis with visualizations.

3. **Numerical Data Analysis**
   - Create a correlation matrix and thermogram, and perform a pairs plot analysis. This step highlights key numerical relationships, such as the correlation between different types of energy consumption and the target variable, GHG emissions.

### Variable Comparisons with GHG Emission
- **Building Types** vs. GHG Emission
- **Building Age** vs. GHG Emission
- **Number of Buildings** vs. GHG Emission
- **Operating Occupancy** vs. GHG Emission

### Missing Values
There is a remaining missing value treatment step. To avoid data leakage, missing values will be addressed during model training and machine learning.

---
