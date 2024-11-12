import random

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

data = pd.read_csv("/Users/hester/Desktop/data_clean.csv")

random.seed(123)
np.random.seed(123)

# Define features and target variable
features = [
    'Primary Property Type - Self Selected',
    'Largest Property Use Type',
    'Primary Property Use Type - Gross Floor Area (ft²)',
    'Year Built',
    'Number of Buildings - Self-reported',
    'Occupancy',
    'Water Intensity (All Water Sources) (gal/ft²)',
    'age',
    'age_group',
    'Occupancy_group',
    'Latitude',
    'Longitude',
    'Site EUI (kBtu/ft²)',
    'Weather Normalized Site Electricity Intensity (kWh/ft²)',
    'Weather Normalized Site Natural Gas Intensity (therms/ft²)',
    'Water Use (All Water Sources) (kgal)'
]
target = 'GHG Emissions'
data = data.dropna(subset=[target])

# Split the dataset into features and target variable
X = data[features]
y = data[target]
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
# Select numerical and categorical features
num_features = X.select_dtypes(include=['int64', 'float64']).columns
cat_features = X.select_dtypes(include=['object']).columns

# Preprocessing pipeline for missing values
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine numerical and categorical preprocessing steps
preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
    ])

# Define multiple regression models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=123),
    "Random Forest": RandomForestRegressor(random_state=123),
    "XGBoost": XGBRegressor(random_state=123, use_label_encoder=False, eval_metric='rmse')
}

results = []
for model_name, model in models.items():
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', model)
    ])
    # Train the model
    pipeline.fit(X_train, y_train)
     # Predict the test set results
    y_pred = pipeline.predict(X_test)
     # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    # Append results to the list
    results.append({
        "Model": model_name,
        "MSE": mse,
        "RMSE": rmse,
        "R2 Score": r2
    })

results_df = pd.DataFrame(results)

from sklearn.model_selection import GridSearchCV  # Import GridSearchCV for hyperparameter tuning

# Define the hyperparameter grid for RandomForestRegressor
param_grid_rf = {
    'regressor__n_estimators': [50, 100, 200],  # Number of trees in the random forest
    'regressor__max_depth': [5, 10, 15]  # Maximum depth of the tree
}

# Define the hyperparameter grid for XGBRegressor
param_grid_xgb = {
    'regressor__n_estimators': [50, 100, 200],  # Number of boosting rounds
    'regressor__max_depth': [3, 5, 7],  # Maximum depth of a tree
    'regressor__learning_rate': [0.01, 0.1, 0.2]  # Learning rate (step size shrinkage)
}

# Set up GridSearchCV for RandomForestRegressor
grid_rf = GridSearchCV(
    Pipeline([('preprocessor', preprocessor), ('regressor', RandomForestRegressor(random_state=123))]),  # Pipeline with preprocessing and model
    param_grid=param_grid_rf,  # Hyperparameter grid
    cv=5,  # Number of cross-validation folds
    scoring='neg_mean_squared_error'  # Scoring metric to use (negative mean squared error)
)

# Set up GridSearchCV for XGBRegressor
grid_xgb = GridSearchCV(
    Pipeline([('preprocessor', preprocessor), ('regressor', XGBRegressor(random_state=123, use_label_encoder=False))]),  # Pipeline with preprocessing and model
    param_grid=param_grid_xgb,  # Hyperparameter grid
    cv=5,  # Number of cross-validation folds
    scoring='neg_mean_squared_error'  # Scoring metric to use (negative mean squared error)
)

# Fit GridSearchCV for RandomForestRegressor on training data
grid_rf.fit(X_train, y_train)

# Fit GridSearchCV for XGBRegressor on training data
grid_xgb.fit(X_train, y_train)

# Get the best estimator for RandomForestRegressor
best_rf = grid_rf.best_estimator_

# Get the best estimator for XGBRegressor
best_xgb = grid_xgb.best_estimator_

encoded_features = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(cat_features)
all_features = num_features.tolist() + encoded_features.tolist()

xgb_importances = best_xgb.named_steps['regressor'].feature_importances_

xgb_importances_df = pd.DataFrame({
    'Feature': all_features,
    'Importance': xgb_importances
}).sort_values(by='Importance', ascending=False)

encoded_features = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(cat_features)
all_features = num_features.tolist() + encoded_features.tolist()

rf_importances = best_rf.named_steps['regressor'].feature_importances_

rf_importances_df = pd.DataFrame({
    'Feature': all_features,
    'Importance': rf_importances
}).sort_values(by='Importance', ascending=False)

top_10_xgb_features = xgb_importances_df.head(10)['Feature'].tolist()
top_10_rf_features = rf_importances_df.head(10)['Feature'].tolist()

important_features = list(set(top_10_xgb_features) & set(top_10_rf_features))

X_train_important = X_train[important_features]
X_test_important = X_test[important_features]

final_rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

final_rf.fit(X_train_important, y_train)

final_xgb = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    use_label_encoder=False,
    eval_metric='rmse'
)

final_xgb.fit(X_train_important, y_train)

y_pred_rf = final_rf.predict(X_test_important)
rmse_rf = mean_squared_error(y_test, y_pred_rf, squared=False)
r2_rf = r2_score(y_test, y_pred_rf)


y_pred_xgb = final_xgb.predict(X_test_important)
rmse_xgb = mean_squared_error(y_test, y_pred_xgb, squared=False)
r2_xgb = r2_score(y_test, y_pred_xgb)


base_prediction = final_xgb.predict(X_train_important).mean()


sensitivity_results = {}
for feature in important_features:
    results = []
    for change in [-0.2, -0.1, 0, 0.1, 0.2]:
        X_modified = X_train_important.copy()
        X_modified[feature] = X_train_important[feature] * (1 + change)
        modified_prediction = final_xgb.predict(X_modified).mean()
        results.append(modified_prediction - base_prediction)
    sensitivity_results[feature] = results

sensitivity_df = pd.DataFrame(sensitivity_results, index=["-20%", "-10%", "Base", "+10%", "+20%"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
for feature, values in sensitivity_results.items():
    ax.plot(["-20%", "-10%", "Base", "+10%", "+20%"], values, label=feature, marker='o')
ax.axhline(0, color='gray', linestyle='--', label="Base Prediction")
ax.set_xlabel("Feature Change")
ax.set_ylabel("Change in Predicted GHG Emissions")
ax.set_title("Sensitivity Analysis of GHG Emissions")
ax.legend()
plt.show()


