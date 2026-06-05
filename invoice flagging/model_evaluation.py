from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, make_scorer, f1_score, confusion_matrix

def train_random_forest(X_train, y_train):
    rf = RandomForestClassifier(random_state=42, n_jobs=-1)
    
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    }
        
    grid_search = GridSearchCV(
        estimator=rf, 
        param_grid=param_grid,
        scoring="accuracy",
        cv=5,
        n_jobs=-1
    ) 
    
    grid_search.fit(X_train, y_train)
    return grid_search

def evaluate_classifier(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)

    print(f"\n{'='*50}")
    print(f"Model: {model_name}")
    print(f"{'='*50}")

    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_pred, y_test))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))