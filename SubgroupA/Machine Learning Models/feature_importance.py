import pandas as pd

def get_feature_importance(model, num_features):
    importances = model.named_steps['regressor'].feature_importances_
    importances_df = pd.DataFrame({
        'Feature': num_features,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    return importances_df