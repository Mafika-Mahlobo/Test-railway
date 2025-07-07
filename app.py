from flask import Flask, render_template, request
import os
from services.compute_results import total_surveys, average_age, oldest, youngest, pizza, pasta, pap_wors, movie, radio, tv, eating_out

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/results")
def survery_results():

    total = total_surveys()
    if (total == 0):
        return render_template("results.html", results_message="No Surveys Available.")
    ave_age = round(average_age(), 2)
    max_name = oldest()[0]
    max_age = oldest()[1]
    min_name = youngest()[0]
    min_age = youngest()[1]
    pizza_percentage = round(pizza(), 1)
    pasta_percentage = round(pasta(), 1)
    pap_wors_percentage = round(pap_wors(), 1)
    movies_rate = round(movie(), 1)
    radio_rate = round(radio(), 1)
    eat_out_rate = round(eating_out(), 1)
    tv_rate = round(tv(), 1)
    return render_template("results.html",
    total=total, average_age=ave_age, old_name=max_name, 
    old_age=max_age, young_name=min_name, young_age=min_age, 
    pizza=pizza_percentage, pasta=pasta_percentage, pap=pap_wors_percentage, movie_rating=movies_rate, radio=radio_rate, eat=eat_out_rate, tv=tv_rate)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)