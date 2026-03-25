import os
from datetime import datetime
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://60095061:12student34@cluster0.wifobkq.mongodb.net/")
DB_NAME = os.getenv("DB_NAME", "projectINFS3203_db")

