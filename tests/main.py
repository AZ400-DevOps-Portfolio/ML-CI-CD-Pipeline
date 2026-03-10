# main.py
# Serves the trained Iris model as a REST API using FastAPI.
# The /predict endpoint accepts flower measurements and returns a predicted species.

import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Iris Model API",
    description="ML model deployment demo for AZ-400 DevOps portfolio",
    version="1.0.0"
)

# Load the trained model at startup
with open("model/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

# Species labels
SPECIES = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.get("/")
def root():
    return {"message": "Iris Model API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(features: IrisFeatures):
    input_data = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0].max()

    return {
        "species": SPECIES[prediction],
        "confidence": round(float(probability), 2),
        "model_version": "1.0.0"
    }