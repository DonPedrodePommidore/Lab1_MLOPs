import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    X, y = load_iris(return_X_y=True)
    return X, y
def train_model(X, y):
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model
def save_model(model, filename="model.joblib"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    print("laduje dane")
    X, y = load_data()
    print("trenuje modell")
    trained_model = train_model(X, y)
    print("zapisuje model")
    save_model(trained_model)