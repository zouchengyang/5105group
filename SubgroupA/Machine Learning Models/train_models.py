from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train_models(models, X_train, y_train, X_test, y_test, preprocessor):
    results = []
    for model_name, model in models.items():
        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', model)
        ])
        
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        r2 = r2_score(y_test, y_pred)

        results.append({
            "Model": model_name,
            "MSE": mse,
            "RMSE": rmse,
            "R2 Score": r2
        })
    
    return pd.DataFrame(results)