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
        probability = self.model.predict_proba(pred_basis)
        return prediction, probability

    def save(self, filepath):
        saved_model = joblib.dump(self.model, filepath)
        return saved_model

    @staticmethod
    def open(filepath):
        loaded_model = joblib.load(filepath)
        return loaded_model
    
    def info(self):
        return f"Base Model: {self.name} \nTimestamp: {datetime.now()}"
