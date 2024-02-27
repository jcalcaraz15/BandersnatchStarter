import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from datetime import datetime
from data import MongoDB


class Machine:
    """
    A class representing a Random Forest Classifier machine learning model.
    """

    def __init__(self, df: pd.DataFrame):
        # Initialize attributes
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now()
        # Preprocess data
        target = df['Rarity']
        features = df.drop(columns=['Rarity'])
        # Train Model
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    # def retrain(self, model):
    #     model = open

    def __call__(self, pred_basis: pd.DataFrame):
        # Predicts the rarity of items based on input features.
        prediction, *_ = self.model.predict(pred_basis)
        confidence, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(confidence)

    def save(self, filepath: str):
        # Saves the model to a file using joblib.
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath: str):
        # Loads a saved model from a file using joblib.
        model = joblib.load(filepath)
        return model

    def info(self):
        # Returns model name and timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
        return f"Base Model: {self.name} <br> Timestamp: {timestamp}"
