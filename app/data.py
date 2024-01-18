from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
import random
from datetime import datetime


class Database:
    load_dotenv()
    database = MongoClient(getenv("CONNECTION_STR"), tlsCAFile=where())["Database"]
    
    def __init__(self, database, library = Monster):
        #instantiate inputs for our database and Data source
        self.database = database
        self.library = library

    def seed(self, amount = 1000):
        #correctly inserts the specified number of monsters into the
        #collection
        document = {}

        for _ in range(amount):
            for column_name in self.library.items():
                document[column_name] = random.choice(Monster)

        document["timestamp"] = datetime.utcnow()

        self.database.insert_one(document)

    def reset(self):
        #correctly deletes all monsters from the collection

    def count(self) -> int:
        #correctly return sht enumber of monsters in the collection

    def dataframe(self) -> DataFrame:
        #correclty returns a DataFrame containing all monsters in the
        #collection

    def html_table(self) -> str:
        #correctly returns an HTML table representation of the DataFrame or
        #None if the collection is empty
