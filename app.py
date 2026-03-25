from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "projectINFS3203 is running"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/test-db")
def test_db():
    try:
        from services.db import get_notes_collection
        col = get_notes_collection()
        col.insert_one({"test": "connection"})
        return {"status": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)