def evaluate_model(model, X_test, y_test):
    """Sample evaluation function for ML models."""
    y_pred = model.predict(X_test)
    accuracy = (y_pred == y_test).mean()
    print(f"Accuracy: {accuracy:.2f}")
    return accuracy 