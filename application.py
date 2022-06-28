import pandas
import numpy
import sys
import os
sys.path.append(".")
from flask import Flask, render_template, request

# Initiate Flask
application = Flask(__name__,
                    template_folder='templates',
                    static_folder='templates/static')

# === Loading Different Pages ===


# ---> Render Main Website
@application.route("/")
def home():
    return render_template("index.html")


# ---> Render Keyword_Engine
@application.route("/Search_by_keyword")
def to_keyword_engine():
    return render_template('keyword_engine.html')


# ---> Render Phrase Engines
@application.route("/Search_by_meaning")
def to_phrase_engine():
    return render_template('Phrase_engine.html')


# === Iterating Through Pages ===
@application.route("/Results")
def show_results():
    """ Rendering Result to HTML Website"""
    features_ = {
        "word_to_search": None,
        "Category_": None,
        "Time_": None,
        "Match_": None
    }
    if request.method == "POST":
        for key_ in features_.keys():
            features_[key_] = request.form[key_]


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    application.run(debug=True, host="127.0.0.1", port=port)
