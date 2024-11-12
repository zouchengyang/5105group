import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV, cross_val_score
import joblib

from data_preparation import prepare_data
from split_data import split_data
from create_preprocessor import create_preprocessor
from train_models import train_models
from perform_grid_search import perform_grid_search
from feature_importance import get_feature_importance
from save_model import save_model

# Data Preparation
file_path = 'data_clean.csv'
X, y = prepare_data(file_path)

# Split Data
X_train, X_test, y_train, y_test = split_data(X, y)

# Preprocessor Creation
num_features = [
    'Site EUI (kBtu/ft²)', 
    'Weather Normalized Site Natural Gas Intensity (therms/ft²)', 
    'Primary Property Use Type - Gross Floor Area (ft²)', 
    'Weather Normalized Site Electricity Intensity (kWh/ft²)', 
    'Latitude', 
    'Longitude'
]
preprocessor = create_preprocessor(num_features, None)

# Models Training
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=123),
    "Random Forest": RandomForestRegressor(random_state=123),
    "XGBoost": XGBRegressor(random_state=42, use_label_encoder=False, eval_metric='rmse')
}

# Train models and print results
results_df = train_models(models, X_train, y_train, X_test, y_test, preprocessor)
print(results_df)

# Perform Grid Search for Hyperparameter Tuning
best_rf, best_xgb = perform_grid_search(X_train, y_train, preprocessor)

# Feature Importance Analysis
rf_importances_df = get_feature_importance(best_rf, num_features)
xgb_importances_df = get_feature_importance(best_xgb, num_features)

print("Top Random Forest Features:\n", rf_importances_df)
print("Top XGBoost Features:\n", xgb_importances_df)

# Save the best model
save_model(best_rf, 'best_rf_model.pkl')

