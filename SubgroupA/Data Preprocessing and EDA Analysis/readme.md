# Data Preprocessing and EDA Analysis

This repository contains `data_processing.py`, a Python script that performs data preprocessing and exploratory data analysis (EDA) on building energy and emissions data. The script prepares raw data for machine learning modeling by cleaning, transforming, and analyzing the data. The final cleaned dataset is saved as `data_clean.csv`.

## Workflow Overview

### 1. Data Loading
The script starts by loading raw data from an Excel file using the `load_data()` function.

### 2. Data Cleaning and Transformation
The following steps are applied to clean and prepare the data:
- **Drop Unnecessary Columns**: Irrelevant columns such as "Order," "Property Id," and "BBL - 10 digits" are removed.
- **Replace Missing Entries**: Entries labeled "Not Available" are converted to `NaN` to indicate missing data.
- **Convert Columns to Numeric**: Columns that contain numerical values (e.g., in square feet, kBtu, Metric Tons CO2e, kWh, therms, etc.) are converted to `float` for consistent data types.
- **Replace Negative Values**: Any negative values in fields that logically should be non-negative (e.g., emissions and usage data) are replaced with `NaN`.
- **Identify and Handle Missing Values**: Missing values per column are calculated and displayed, providing insights into data completeness.
- **Rename Columns**: Certain columns are renamed for clarity, including "Total GHG Emissions," "Direct GHG Emissions," and "Indirect GHG Emissions."

### 3. Exploratory Data Analysis (EDA)
The script conducts EDA on the processed data to uncover patterns and relationships. Key steps include:
- **Distribution Analysis**: The script plots histograms for the distribution of GHG emissions, both in raw and log-transformed form.
- **Outlier Processing**: Outliers are identified and removed based on the IQR (Interquartile Range) method.
- **Correlation Analysis**: A correlation matrix and thermogram are generated to visualize relationships between numerical features.
- **Pair Plot Analysis**: Pair plots allow for a preliminary observation of key variable relationships, focusing on energy consumption metrics and GHG emissions.
- **Density Plots by Building Type**: Distribution of log-transformed GHG emissions across different building types is visualized using density plots.
- **Analysis by Building Age**: A heatmap is generated to show the relationship between building age groups and GHG emissions.
- **Box Plots by Building Count and Occupancy**: Box plots are used to analyze GHG emissions by the number of buildings and occupancy rates.

### 4. Data Output
The final cleaned dataset, after outlier removal and transformation, is saved as `data_clean.csv`. This file is ready for further machine learning modeling and analysis.

## Code Overview

Below is a brief description of key functions in `data_processing.py`:

- `load_data(file_path, sheet_name)`: Loads data from an Excel file.
- `drop_unnecessary_columns(df, columns)`: Drops specified columns from the DataFrame.
- `replace_not_available(df)`: Replaces "Not Available" entries with `NaN`.
- `convert_columns_to_numeric(df)`: Converts columns containing numerical values to `float` type.
- `replace_negative_values(df, features)`: Replaces negative values in specified columns with `NaN`.
- `missing_values(df)`: Calculates missing values per column and displays the results.
- `rename_columns(df)`: Renames specific columns for improved clarity.
- `plot_ghg_distribution(df)`: Plots a histogram of GHG emissions.
- `plot_log_ghg_distribution(df)`: Plots a histogram of log-transformed GHG emissions.
- `outliers_processing(df, columns)`: Identifies and removes outliers based on the IQR method.
- `plot_correlation_matrix(df)`: Displays a correlation matrix for numerical features.
- `plot_pairplot(df)`: Generates a pair plot for key variables and GHG emissions.
- `plot_density_by_building_type(df)`: Plots density of GHG emissions by building type.
- `create_age_group(df)`: Categorizes buildings by age group and plots GHG emissions by age.
- `plot_box_by_building_count(df)`: Box plot of GHG emissions by the number of buildings.
- `plot_box_by_occupancy(df)`: Box plot of GHG emissions by occupancy rate.

## How to Run the Script

1. Place the `data_processing.py` script in the desired directory.
2. Update the `file_path` and `sheet_name` variables in the `main()` function to match the path and sheet name of your raw data file.
3. Run the script:
   ```bash
   python data_processing.py
