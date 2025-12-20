#This file contains the MongoDB code
from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus("dbKaustubh")
password = urllib.parse.quote_plus("Kaustubh@05")

client = MongoClient(f"mongodb+srv://{username}:{password}@typingtest.6cqssqe.mongodb.net/?appName=typingTest")

db = client.todo_db

collection_name = db['todo_collection']

