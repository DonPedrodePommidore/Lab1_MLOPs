import joblib
import numpy as np

types = ["type_1", "type_2", "type_3"]


def load_model(filename="model.joblib"):
    return joblib.load(filename)

def predict(model, input_data: dict) -> str:
    dimensions = [
        input_data["sepal_length"], input_data["sepal_width"], input_data["petal_length"], input_data["petal_width"]
                ]
    dimensions_2d = np.array(dimensions).reshape(1, -1)
    prediction_idx = model.predict(dimensions_2d)[0]

    return types[prediction_idx]