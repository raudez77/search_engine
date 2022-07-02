import sys
sys.path.append(".")
from typing import List
from search_engines.data_manager import database, load_pipeline
from search_engines.data_base.core import COLUMNS, TRAINED_MODEL_DIR
from search_engines.enconding_functions import WordEmbedding_Comparing, Top_Results
import pandas
import re


def search_bar_keywords(*, keywords: str, category: str) -> pandas.DataFrame:
    """filter based on differnet keywords and categories
    Arg: 
        database : import database
        keywords: must be string 
        category: must be string (optional)"""

    # Connecting to Database
    tmp_filter = database

    # limiting the Data by Frist Criteria and Kewords
    both_keyword_category = [bool(keywords) == True, bool(category) == True]
    only_keyword = [bool(keywords) == True, bool(category) == False]
    only_category = [bool(keywords) == False, bool(category) == True]
    all_keywords = r'\b(?:{})\b'.format('|'.join(
        map(re.escape,
            keywords.lower().split(" "))))

    if all(both_keyword_category):
        tmp_criteria = [
            str('category_') + str(name)
            for name in category.lower().split(" ")
        ]
        tmp_filter = tmp_filter[(tmp_filter[tmp_criteria] == 1).any(axis=1)]
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords)]
        return tmp_filter[COLUMNS]  # type: ignore

    elif all(only_keyword):
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords)]
        return tmp_filter[COLUMNS]  # type: ignore

    elif all(only_category):
        tmp_criteria = [
            str('category_') + str(name)
            for name in category.lower().split(" ")
        ]
        tmp_filter = tmp_filter[(tmp_filter[tmp_criteria] == 1).any(axis=1)]
        return tmp_filter[COLUMNS]


def search_bar_meaning(*,
                       keywords: str,
                       category: str = None) -> pandas.DataFrame:

    # Enconding query
    pipe = load_pipeline(file_name="FIT_BBC_NEWS_2200_CORPUS_1.pkl")
    corpus_transformed = load_pipeline(
        file_name="CORPUS_BBC_NEWS_2200_CORPUS_1.pkl")

    # Adding Steps
    pipe.steps.append(
        ["Comparing",
         WordEmbedding_Comparing(corpus=corpus_transformed)])
    pipe.steps.append(["Top_Results", Top_Results()])

    # Comparing
    indexes = pipe.fit_transform(keywords)

    return database.iloc[indexes][COLUMNS]  # type: ignore
