import pathlib
import sys
sys.path.append(".")

DATA_BASE_LOCATION = pathlib.Path(__file__).resolve().parent
NAME = "bbc-tokenized.csv"
COLUMNS = ['title', 'content']
TRAINED_MODEL_DIR = DATA_BASE_LOCATION.parent / "trained"
VERSION = "1"