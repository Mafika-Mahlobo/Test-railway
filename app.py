from flask import Flask, render_template, request
import os
from services.compute_results import total_surveys, average_age, oldest, youngest, pizza, pasta, pap_wors, movie, radio, tv, eating_out
from services.validate_input import check_email
from services.save_survey import add

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/results")
def survery_results():

    total = total_surveys()
    print(total)
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

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["fullname"]
        email = request.form["email"]
        age = request.form["age"]
        phone = request.form["phone_number"]

        pizza = int(request.form.get("pizza", "0"))
        pasta = int(request.form.get("pasta", "0"))
        pap = int(request.form.get("pap", "0"))
        other = int(request.form.get("pizza", "0"))

        movie = int(request.form["movie"])
        radio = int(request.form["radio"])
        eat = int(request.form["eat"])
        tv = int(request.form["tv"])

        data = (name, email, age, phone, pizza, pasta, pap, other, movie, radio, eat, tv)

        validate_email = check_email((email,))
        if (not validate_email == True):
            response = add(data)

            if (response == True):
                return render_template("index.html", success="Thank you for your contribution!")
            if (not response == True):
                return render_template("index.html", error=response)
            else:
                return render_template("index.html", error=response)
            
        return render_template("index.html", error="You have already submitted your response")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)