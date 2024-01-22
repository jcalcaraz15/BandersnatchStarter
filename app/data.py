from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
import pandas as pd
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    A class that is used to generate a randomized database of
    monsters with different valued columns both numerical and text.
    """


    load_dotenv()

    def __init__(self, collection: str):
        """
        Establishes a connection with our database.
        """
        self.database = MongoClient(getenv("CONNECTION_STR"),
                                    tlsCAFile=where())["Database"]
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
        return self.collection.delete_many({})

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
        return pd.DataFrame(list(self.collection.find({})))

    def html_table(self) -> str:
        """
        Correctly returns an HTML table representation of the
        DataFrame or None if the collection is empty.
        """
        if self.count() > 0:
            return self.dataframe().to_html()
        else:
            return None