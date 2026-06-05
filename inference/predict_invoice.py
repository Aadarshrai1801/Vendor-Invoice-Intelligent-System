import joblib
import pandas as pd

MODEL_PATH = "C:/Users/Aadarsh/Desktop/Vendor Invoice Intelligent System/models/invoice_model.pkl"

def load_model(model_path: str=MODEL_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.
    
    Parameters
    ----------
    input_data: dict
    
    Returns
    -------
    pd.DataFrame with predicted flag
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df["Predicted_Flag"] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
    # Example inference run(local testing)
    sample_data = {
        "Quantity": [1055440],
        "Dollars": [18],
        "Freight": [50],
        "days_po_to_invoice": [7000],
        "days_to_pay": [150]
    }
        
    prediction = predict_invoice_flag(sample_data)
    print(prediction)