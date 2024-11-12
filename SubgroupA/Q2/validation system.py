# Re-import necessary libraries and reload datasets to ensure all required data is available
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold

data = pd.read_csv("/Users/hester/Desktop/X_test_data.csv")
# Define the emission factor benchmark ranges for each building type
emission_factors = {
    "Adult Education": (3, 7),
    "Automobile Dealership": (8, 12),
    "College/University": (3, 7),
    "Courthouse": (5, 10),
    "Distribution Center": (2, 5),
    "Enclosed Mall": (8, 12),
    "Hospital (General Medical & Surgical)": (10, 15),
    "Hotel": (6, 12),
    "K–12 School": (3, 7),
    "Library": (3, 7),
    "Mailing Center/Post Office": (5, 10),
    "Manufacturing/Industrial Plant": (5, 10),
    "Medical Office": (5, 10),
    "Multifamily Housing": (4, 8),
    "Museum": (3, 7),
    "Non–Refrigerated Warehouse": (2, 5),
    "Office": (5, 10),
    "Other – Education": (3, 7),
    "Other – Entertainment/Public Assembly": (6, 12),
    "Other – Lodging/Residential": (5, 10),
    "Other – Mall": (8, 12),
    "Other – Public Services": (5, 10),
    "Other – Recreation": (5, 10),
    "Other – Specialty Hospital": (10, 15),
    "Outpatient Rehabilitation/Physical Therapy": (10, 15),
    "Retail Store": (8, 12),
    "Self–Storage Facility": (2, 5),
    "Senior Care Community": (5, 10),
    "Social/Meeting Hall": (5, 10),
    "Strip Mall": (8, 12),
    "Supermarket/Grocery Store": (12, 20),
    "Urgent Care/Clinic/Other Outpatient": (10, 15),
    "Wholesale Club/Supercenter": (8, 12),
    "Worship Facility": (5, 10)
}

# Create new columns for benchmark, lowest emission, and largest emission
data['benchmark'] = data['Largest Property Use Type'].map(lambda x: f"{emission_factors[x][0]} - {emission_factors[x][1]}" if x in emission_factors else None)
data['lowest_emission'] = data['Largest Property Use Type'].map(lambda x: emission_factors[x][0] if x in emission_factors else None)
data['largest_emission'] = data['Largest Property Use Type'].map(lambda x: emission_factors[x][1] if x in emission_factors else None)


# Load the x_test dataset
x_test_path = '/Users/hester/Desktop/x_test.csv'
x_test = pd.read_csv(x_test_path)

# Load the predicted values dataset
y_pred_path = '/Users/hester/Desktop/y_pred_rf.csv'
y_pred = pd.read_csv(y_pred_path)

# Add predicted values to x_test dataset
x_test['predicted_emissions'] = y_pred['Predicted GHG Emissions']

# Perform K-Fold Cross-Validation to validate predicted values against emission benchmarks
kf = KFold(n_splits=5, shuffle=True, random_state=42)
fold_results = []

# Perform K-Fold Cross-Validation to validate predicted values
for train_index, test_index in kf.split(x_test):
    # Split the dataset into train and test sets for this fold
    x_train, x_test_fold = x_test.iloc[train_index], x_test.iloc[test_index]

    # Validate predictions: Check if predicted emissions fall within the benchmark range
    within_benchmark_fold = x_test_fold.apply(
        lambda row: row['min_emission_estimate'] <= row['predicted_emissions'] <= row['max_emission_estimate'],
        axis=1
    )

    # Calculate percentage of buildings that fall within benchmark range for this fold
    percentage_within_benchmark_fold = within_benchmark_fold.sum() / len(x_test_fold) * 100
    fold_results.append(percentage_within_benchmark_fold)

# Calculate the overall average percentage within benchmark across all folds
average_within_benchmark = np.mean(fold_results)

# Display the results of cross-validation
cross_validation_summary = {
    "Total Folds": kf.get_n_splits(),
    "Percentage Within Benchmark (Per Fold)": fold_results,
    "Overall Average Percentage Within Benchmark": average_within_benchmark
}

print(cross_validation_summary)
