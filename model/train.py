# train.py
# Trains a simple Iris classifier and saves it as a .pkl file.
# In a real MLOps pipeline, this would be triggered by new training data.

import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

def train_model():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model accuracy: {accuracy:.2f}")

    # Save model
    os.makedirs("model", exist_ok=True)
    with open("model/iris_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved to model/iris_model.pkl")

if __name__ == "__main__":
    train_model()