import sys
sys.path.append(".")
from search_engines.enconding_functions import *
from search_engines.data_base.core import DATA_BASE_LOCATION, NAME, PRE_TRAINED_MODEL
from search_engines.data_manager import database, save_pipelines
import sklearn.pipeline



# Transfoming Data
Pipe_train = sklearn.pipeline.Pipeline([
    ("Emebdding Query", WordEmbedding_Transformer(pre_train_model_path = PRE_TRAINED_MODEL))
])

# Saving Pipelines
save_pipelines(pipeline_to_save=Pipe_train.fit_transform(database.content),
               pipeline_name="CORPUS_BBC_NEWS_2200_CORPUS_",
               version="1",
               remove_previous_version=False)

