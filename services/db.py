import os
from datetime import datetime
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "projectINFS3203_db")


def get_notes_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db["notes"]


def save_note(text):
    collection = get_notes_collection()
    note = {
        "text": text,
        "created_at": datetime.utcnow()
    }
    collection.insert_one(note)


def list_notes():
    collection = get_notes_collection()
    notes = []

    for note in collection.find().sort("created_at", -1):
        notes.append({
            "text": note.get("text", ""),
            "created_at": note.get("created_at")
        })

    return notes