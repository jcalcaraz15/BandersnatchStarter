from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
import pandas as pd
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(getenv("CONNECTION_STR"),
                           tlsCAFile=where())["Database"]
    
    def __init__(self, collection: str):
        """establishes a connection between our database and the input"""
        self.collection = self.database[collection]

    def seed(self, amount = 1000):
        """correctly inserts the specified number of monsters into the
        collection, uses a built in mongo function"""
        Monsters = [Monster().to_dict() for _ in range(amount)]
        MonsterBook = self.collection.insert_many(Monsters)
        return f"{MonsterBook.acknowledged}"

    def reset(self):
        """correctly deletes all monsters from the collection
        mongo functions we want to leave it an empty database delete
        collection, built in mongo function"""
        return self.collection.delete_many({})
        
    def count(self) -> int:
        """correctly returns the number of monsters in the collection
        mongo db count indices of dictionary or collection, count_documents
        self.collection.count_documents(Filter={}) built in mongo function"""
        return self.collection.count_documents({})
    
    def dataframe(self) -> DataFrame:
        """correctly returns a DataFrame containing all monsters in the
        collection
        return a pandas dataframe df = pd.DataFrame(self.collection.find)
        built in pandas function and then usage of find inside the pandas
        function which is a mongo function"""
        return pd.DataFrame(list(self.collection.find({})))
        
    def html_table(self) -> str:
        """correctly returns an HTML table representation of the DataFrame or
        None if the collection is empty pandas function that converts to html
        dataframe.to_html() if count > 0 then return self.dataframe else
        return None usage of the other functions to produce a table, taps
        into the mongo table during usage of said functions."""
        if self.count() > 0:
            return self.dataframe().to_html()
        else:
            return None