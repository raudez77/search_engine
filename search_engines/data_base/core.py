import pathlib
import sys
import os
sys.path.append(".")

DATA_BASE_LOCATION = pathlib.Path(__file__).resolve().parent
NAME = "bbc-tokenized.csv"
COLUMNS = ['title', 'content']
TRAINED_MODEL_DIR = DATA_BASE_LOCATION.parent / "trained"
VERSION = "1"
PRE_TRAINED_MODEL = str(os.path.join(TRAINED_MODEL_DIR.parent / "trained/model"))
