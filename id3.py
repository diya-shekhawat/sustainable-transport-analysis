import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def run(data):

    # Target column
    target = "How willing are you to switch to a more sustainable mode of transport?"

    # Remove rows where target is missing
    data = data.dropna(subset=[target]).copy()

    # Separate input and output
    X = data.drop(columns=[target])
    y = data[target]

    # Convert text columns into numbers
    X = pd.get_dummies(X, drop_first=True)

    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # ID3 Decision Tree
    model = DecisionTreeClassifier(
        criterion="entropy",
        random_state=42
    )

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Confusion matrix
    matrix = confusion_matrix(y_test, y_pred)

    # Feature importance
    importance = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    # Root attribute
    root = X.columns[model.tree_.feature[0]]

    return {
        "model": model,
        "accuracy": accuracy,
        "confusion_matrix": matrix,
        "feature_importance": importance,
        "root": root,
        "features": X.columns
    }