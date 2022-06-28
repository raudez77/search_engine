import sys
sys.path.append(".")
from search_engines.engines import search_bar_keywords

print(search_bar_keywords(keywords=["music"], Category=['business']))
