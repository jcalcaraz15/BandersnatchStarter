import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime


class Machine:

    def __init__(self, df: pd.DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=7)
        self.model.fit(features, target)
        self.timestamp = datetime.now()

    def __call__(self, pred_basis: pd.DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        confidence, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        model = joblib.load(filepath)
        return model

    def info(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
        return f"Base Model: {self.name}<br>Timestamp: {timestamp}"
