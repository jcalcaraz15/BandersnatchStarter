from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
import pandas as pd
from pandas import DataFrame
from pymongo.mongo_client import MongoClient


class Database:
    """
    A class that is used to generate a randomized database of
    monsters with different valued columns both numerical and text.
    """


    load_dotenv()

    database = MongoClient(getenv("CONNECTION_STR"),
                                    tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        """
        Establishes a connection with our database.
        """
        self.collection = self.database[collection]

    def seed(self, amount = 1000):
        """
        Correctly inserts the specified number of monsters into the
        collection.
        """
        Monsters = [Monster().to_dict() for _ in range(amount)]
        MonsterBook = self.collection.insert_many(Monsters)
        return f"{MonsterBook.acknowledged}"

    def reset(self):
        """
        Correctly deletes all monsters from the collection.
        """
        return f"{self.collection.delete_many(filter={}).acknowledged}"

    def count(self) -> int:
        """
        Correctly returns the number of monsters in the
        collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Correctly returns a DataFrame containing all monsters in
        the collection.
        """
        return pd.DataFrame(list(self.collection.find({}, {"_id":False})))

    def html_table(self) -> str:
        """
        Correctly returns an HTML table representation of the
        DataFrame or None if the collection is empty.
        """
        if self.count() > 0:
            return self.dataframe().to_html(index=False)
        else:
            return None
        
if __name__ == '__main__':
    db = Database("Collection")
    db.seed()
