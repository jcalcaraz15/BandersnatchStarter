""" Monster Database Interface """
from os import getenv
from typing import Dict, Iterable, Iterator
import pandas as pd
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class MongoDB:
    """ A class representing a MongoDB database connection and operations on a specific collection. """
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())['BandersnatchStarter']

    def __init__(self, collection: str):
        """ Initialize the MongoDB instance with a specific collection. """
        self.collection = self.database[collection]

    def insert_one(self, document: Dict) -> bool:
        """ Insert a single document into the collection. """
        return self.collection.insert_one(document).acknowledged

    def insert_many(self, documents: Iterable[Dict]) -> bool:
        """ Insert multiple documents into the collection. """
        return self.collection.insert_many(documents).acknowledged

    def read_one(self, query: Dict) -> Dict:
        """ Retrieve a single document based on the query. """
        return self.collection.find_one(query, {"_id": False})

    def read_many(self, query: Dict) -> Iterator[Dict]:
        """ Retrieve multiple documents based on the query. """
        return self.collection.find(query, {"_id": False})

    def update_one(self, query: Dict, update: Dict) -> bool:
        """ Update a single document based on the query. """
        return self.collection.update_one(query, {"$set": update}).acknowledged

    def update_many(self, query: Dict, update: Dict) -> bool:
        """ Update multiple documents based on the query. """
        return self.collection.update_many(query, {"$set": update}).acknowledged

    def delete_one(self, query: Dict) -> bool:
        """ Delete a single document based on the query. """
        return self.collection.delete_one(query).acknowledged

    def delete_many(self, query: Dict) -> bool:
        """ Delete multiple documents based on the query. """
        return self.collection.delete_many(query).acknowledged

    def seed(self, amount):
        """ Inserts the specified number of documents into the collection """
        add_list = []
        monster_count = 0
        for _ in range(amount):
            monster = Monster()
            monster_data = {
                "Name": monster.name,
                "Type": monster.type,
                "Level": monster.level,
                "Rarity": monster.rarity,
                "Damage": monster.damage,
                "Health": monster.health,
                "Energy": monster.energy,
                "Sanity": monster.sanity,
                "Timestamp": monster.timestamp
            }
            add_list.append(monster_data)
            monster_count += 1

        result = self.collection.insert_many(add_list)
        print(f"There were {monster_count} documents inserted.")

    def reset(self):
        """ Drop the entire collection to clear all documents """
        self.collection.drop()
        print(f"Collection '{self.collection.name}' has been reset.")

    def count(self) -> int:
        """ Count all documents in collection """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """ Create Pandas DataFrame from mongoDB collection """
        documents = list(self.collection.find())
        df = pd.DataFrame(documents)
        return df

    def html_table(self) -> str:
        """ Return the pandas dataframe in a html formatted table. """
        df = self.dataframe()

        if df.empty:
            return "None"

        df = df.drop(columns=['_id'], errors='ignore')
        html_table = df.to_html(index=True)
        return html_table


if __name__ == '__main__':

    db = MongoDB("Collection")
    # db.seed(amount=10000)
    #
    # db.reset()

    # pandas_df = db.dataframe()

    # if isinstance(pandas_df, pd.DataFrame):
    #     print("df is a Pandas DataFrame")
    # else:
    #     print("df is not a Pandas DataFrame")

    # html = db.html_table()
    # print(html)
