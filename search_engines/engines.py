from feature_engine.encoding import OneHotEncoder
from search_engines.data_manager import database
import pandas
import re
import sys
sys.path.append(".")


def search_bar_keywords(*, keywords: list, Category: list) -> pandas.DataFrame:
    """Filter based on different keywords
    Arg:
        connection to data base
        keywords: list of keywords
        Category : list of categories"""

    if not isinstance(keywords, list):
        raise ValueError("Keyword must be a list")

    if not isinstance(Category, list):
        raise ValueError("Vategory must be a list")

    # Connecting to Database
    tmp_filter = database

    # limiting the Data by Frist Criteria and Kewords
    search = [bool(keywords) == True, bool(Category)]
    all_keywords = r'\b(?:{})\b'.format('|'.join(map(re.escape, keywords)))
    cols_return = ['title', 'content', 'filename']

    if all(search):
        tmp_criteria = [
            str('category_') + str(name).lower() for name in Category
        ]
        tmp_filter = tmp_filter[(tmp_filter[tmp_criteria] == 1).any(axis=1)]
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords.lower())]
        return tmp_filter[cols_return]
    else:
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords.lower())]
        return tmp_filter[cols_return]
