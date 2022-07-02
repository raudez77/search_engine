from search_engines.data_base.core import DATA_BASE_LOCATION, NAME, TRAINED_MODEL_DIR
import sklearn
import pandas
import joblib
import sys
sys.path.append(".")


def save_pipelines(*, pipeline_to_save, pipeline_name: str, version: str,
                   remove_previous_version: bool) -> None:
    """ Save the current pipelines
    Save the version model"""

    # Set pipeline save file name
    save_file_name = f"{pipeline_name}{version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    if remove_previous_version:
        remove_old_pipelines(file_to_keep=[save_file_name])
        joblib.dump(pipeline_to_save, save_path)
    else:
        joblib.dump(pipeline_to_save, save_path)


def remove_old_pipelines(*, file_to_keep) -> None:
    """remove ol pipelines"""
    do_not_delete = file_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():  #Iterate through files
        if model_file not in do_not_delete:
            model_file.unlink()  #Delete or remove file


def load_pipeline(*, file_name: str):
    """ Load Pipelines"""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(file_path)
    return trained_model


def connect_to_database():
    """ Initiate Connection to DataBase"""
    database = pandas.read_csv(DATA_BASE_LOCATION / NAME, sep=",")
    return database


database = connect_to_database()
