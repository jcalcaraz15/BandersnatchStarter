from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime


class Machine:
    """
    This class should take in features from our Monsterbook and return a
    prediction for the rarity of the monster based on input factors of
    the other attributes of the monsters.
    """
    
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        probability, *_ = self.model.predict_proba(pred_basis)
        return prediction, max(probability)

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    def open(self, filepath):
        loaded_model = joblib.load(filepath)
        return loaded_model
    
    def info(self):
        ret_str = f"""Base Model: {self.name}\nTimestamp: {datetime.now()}"""
        return ret_str
