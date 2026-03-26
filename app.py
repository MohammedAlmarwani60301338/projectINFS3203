from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    notes = list_notes()
    return render_template("index.html", notes=notes, ai_result=None, error=None)


@app.route("/health")
def health():
    return {"status": "ok", "project": "projectINFS3203"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)