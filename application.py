from flask import Flask, render_template, request
import sys
import os
sys.path.append(".")
from search_engines.engines import search_bar_keywords, search_bar_meaning
from search_engines.web_list import result_html

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
@application.route("/results by keywords", methods=["POST"])
def show_results_keywords():
    """ Rendering Result to HTML Website"""
    features_ = {
        "search_keywords_": None,
        "Category_": None,
        "Time_": None,
        "Match_": None,
    }

    final_results = ''

    if request.method == "POST":
        for key_ in features_.keys():
            try:
                # Collection form
                features_[key_] = request.form[key_]
            except:
                features_['search_keywords_'] = request.form.get(
                    'search_keywords_')
                features_['Category_'] = ""  # type: ignore

        results_ = search_bar_keywords(
            keywords=features_['search_keywords_'],  # type: ignore
            category=features_['Category_'])  # type: ignore

        for query in results_.values:
            final_results += result_html(query[0], query[1])

    return render_template('results.html', final_results=final_results)


@application.route("/results by meaning", methods=["POST"])
def show_results_meaning():
    """ Rendering Result to HTML Website"""
    features_ = {
        "search_keywords_meaning": None,
        "Category_": None,
        "Time_": None,
        "Match_": None,
    }

    render_results_meaning = ''
    if request.method == "POST":

        for key_ in features_.keys():
            try:
                # Collection form
                features_[key_] = request.form[key_]
            except:
                features_['search_keywords_meaning'] = request.form.get(
                    'search_keywords_meaning')
                features_['Category_'] = ""  # type: ignore

        results_ = search_bar_meaning(
            query=features_['search_keywords_meaning'],  # type: ignore
            category=features_['Category_'])  # type: ignore

        for query in results_.values:
            render_results_meaning += result_html(query[0], query[1])

    return render_template('results_meaning.html',
                           render_results_meaning=render_results_meaning)


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    application.run(debug=True, host="127.0.0.1", port=port)
