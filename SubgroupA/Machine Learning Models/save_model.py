import joblib

def save_model(model, file_name):
    """
    Function to save the trained model to a file.
    :param model: The model to save.
    :param file_name: The file name to save the model to.
    """
    joblib.dump(model, file_name)
    print(f"Saved model as '{file_name}'")

