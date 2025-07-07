from flask import Flask, render_template
import os
from services.compute_results import total_surveys

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    return f'DB connection - total surveys: {total_surveys()}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)