from flask import Flask, render_template, request
from services.db import save_note, list_notes
from services.ai import generate_summary

app = Flask(__name__)


@app.route("/")
def home():
    notes = list_notes()
    return render_template("index.html", notes=notes, ai_result=None, error=None)


@app.route("/health")
def health():
    return {"status": "ok", "project": "projectINFS3203"}


@app.route("/notes", methods=["POST"])
def create_note():
    text = request.form.get("text", "").strip()

    if not text:
        notes = list_notes()
        return render_template(
            "index.html",
            notes=notes,
            ai_result=None,
            error="Note cannot be empty."
        ), 400

    save_note(text)
    return home()


@app.route("/ai/summary", methods=["POST"])
def ai_summary():
    text = request.form.get("text", "").strip()

    if not text:
        notes = list_notes()
        return render_template(
            "index.html",
            notes=notes,
            ai_result=None,
            error="Please enter text before generating a summary."
        ), 400

    try:
        result = generate_summary(text)
        notes = list_notes()
        return render_template(
            "index.html",
            notes=notes,
            ai_result=result,
            error=None
        )
    except Exception:
        notes = list_notes()
        return render_template(
            "index.html",
            notes=notes,
            ai_result=None,
            error="Failed to generate AI summary."
        ), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)