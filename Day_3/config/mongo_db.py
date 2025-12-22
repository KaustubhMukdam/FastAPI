#This file contains the MongoDB code
from pymongo import MongoClient
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv(".env")

username = urllib.parse.quote_plus(os.getenv("MONGO_USERNAME"))
password = urllib.parse.quote_plus(os.getenv("MONGO_PASSWORD"))

client = MongoClient(f"mongodb+srv://{username}:{password}@typingtest.6cqssqe.mongodb.net/?appName=typingTest")

db = client.todo_db

collection_name = db['todo_collection']

