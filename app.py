from flask import Flask, render_template, request
from services.db import save_note, list_notes
from services.ai import generate_summary

app = Flask(__name__)


@app.route("/")
def home():
    notes = list_notes()
    return render_template("index.html", notes=notes, ai_result=None, error=None)