from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def perform_grid_search(X_train, y_train, preprocessor):
    param_grid_rf = {
        'regressor__n_estimators': [50, 100, 200],
        'regressor__max_depth': [5, 10, 15]
    }

    param_grid_xgb = {
        'regressor__n_estimators': [50, 100, 200],
        'regressor__max_depth': [3, 5, 7],
        'regressor__learning_rate': [0.01, 0.1, 0.2]
    }

    grid_rf = GridSearchCV(
        Pipeline([('preprocessor', preprocessor), ('regressor', RandomForestRegressor(random_state=123))]),
        param_grid=param_grid_rf, cv=5, scoring='neg_mean_squared_error'
    )

    grid_xgb = GridSearchCV(
        Pipeline([('preprocessor', preprocessor), ('regressor', XGBRegressor(random_state=123, use_label_encoder=False))]),
        param_grid=param_grid_xgb, cv=5, scoring='neg_mean_squared_error'
    )

    grid_rf.fit(X_train, y_train)
    grid_xgb.fit(X_train, y_train)

    return grid_rf.best_estimator_, grid_xgb.best_estimator_