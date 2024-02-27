import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from datetime import datetime


class Machine:

    def __init__(self, df: pd.DataFrame):
        self.name = "Random Forest Classifier"
        df['Rarity'] = df['Rarity'].str.extract('(\d+)')
        target = df["Rarity"].astype(int)
        features = df[['Level', 'Energy', 'Health', 'Sanity']]
        self.model = RandomForestClassifier()
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
        return f"Base Model: {self.name} <br> Timestamp: {timestamp}"

