import sys
sys.path.append(".")
from search_engines.enconding_functions import *
from search_engines.data_base.core import DATA_BASE_LOCATION, NAME
from search_engines.data_manager import database, save_pipelines
import sklearn.pipeline

# Transfoming Data
Pipe_train = sklearn.pipeline.Pipeline([
    ("Emebdding Query", WordEmbedding_Transformer('all-MiniLM-L6-v2'))
])

# Saving Pipelines
save_pipelines(pipeline_to_save=Pipe_train.fit_transform(database.content),
               pipeline_name="CORPUS_BBC_NEWS_2200_CORPUS_",
               version="1",
               remove_previous_version=False)

save_pipelines(pipeline_to_save=Pipe_train,
               pipeline_name="FIT_BBC_NEWS_2200_CORPUS_",
               version="1",
               remove_previous_version=False)
