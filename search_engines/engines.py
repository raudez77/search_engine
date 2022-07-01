from feature_engine.encoding import OneHotEncoder
from search_engines.data_manager import database
import pandas
import re
import sys
sys.path.append(".")


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
    cols_return = ['title', 'content', 'filename']

    if all(both_keyword_category):
        tmp_criteria = [
            str('category_') + str(name)
            for name in category.lower().split(" ")
        ]
        tmp_filter = tmp_filter[(tmp_filter[tmp_criteria] == 1).any(axis=1)]
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords)]
        return tmp_filter[cols_return]  # type: ignore

    elif all(only_keyword):
        tmp_filter = tmp_filter[tmp_filter.content_t.str.contains(
            all_keywords)]
        return tmp_filter[cols_return]  # type: ignore

    elif all(only_category):
        tmp_criteria = [
            str('category_') + str(name)
            for name in category.lower().split(" ")
        ]
        tmp_filter = tmp_filter[(tmp_filter[tmp_criteria] == 1).any(axis=1)]
        return tmp_filter[cols_return]