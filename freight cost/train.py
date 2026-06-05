import joblib
from pathlib import Path
from data_preprocessing import load_vendor_invoice_data, prepare_features, split_data
from model_evaluation import(
    train_linear_regressor,
    train_decision_tree, 
    train_random_forest,
    evaluate_model
)

def main():
    db_path = "C:/Users/Aadarsh/Desktop/Vendor Invoice Intelligent System/data/inventory.db"
    
    # Load data
    df = load_vendor_invoice_data(db_path)
    
    # Prepare data
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train models
    lr_models = train_linear_regressor(X_train, y_train)
    dt_models = train_decision_tree(X_train, y_train)
    rf_models = train_random_forest(X_train, y_train)
    
    # Evaluate models
    results = []
    results.append(evaluate_model(lr_models, X_test, y_test, "Linear Regression"))
    results.append(evaluate_model(dt_models, X_test, y_test, "Decision Tree Regression"))
    results.append(evaluate_model(rf_models, X_test, y_test, "Random Forest Regression"))
    
    # Select best model (lowest MAE)
    best_model_info = min(results, key=lambda x: x["mae"])
    best_model_name = best_model_info["model_name"]
    
    best_model = {
        "Linear Regression": lr_models,
        "Decision Tree Regressor": dt_models,
        "Random Forest Regression": rf_models
    }[best_model_name]
    
    # Save best model
    model_path = "C:/Users/Aadarsh/Desktop/Vendor Invoice Intelligent System/models/freight_model.pkl"
    joblib.dump(best_model, model_path)
    
    print(f"Best model saved: {best_model_name}")
    print(f"Model path: {model_path}")
    
if __name__ == "__main__":
    main()