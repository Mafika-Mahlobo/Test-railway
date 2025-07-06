from flask import Flask, render_template
import os
from services.DBconnection import get_DBconnection

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    conn = get_DBconnection()
    return f"Total Surveys: {conn}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)