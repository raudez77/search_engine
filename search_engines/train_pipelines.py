import sys
sys.path.append(".")
from search_engines.enconding_functions import *
from search_engines.data_manager import database, save_pipelines
import sklearn.pipeline

# Transfoming Data
Pipe_train = sklearn.pipeline.Pipeline([
    ("Emebdding Query", WordEmbedding_Transformer('all-MiniLM-L6-v2'))
])

# Saving Pipelines
Pipe_train.fit_transform(database.content)
save_pipelines(Pipe_train, "BBC_NEWS_2200_CORPUS", "1", False)
