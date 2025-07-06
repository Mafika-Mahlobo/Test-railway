from flask import Flask, render_template
import os
from services.db_test import test_connection

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    status = test_connection()
    return f"Status: "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)