import pandas
import sys
sys.path.append("./")
from data_base.core import DATA_BASE_LOCATION, NAME


def connect_to_database():
    """ Initiate Connection to DataBase"""
    database = pandas.read_csv(DATA_BASE_LOCATION / NAME, sep=",")
    return database


database = connect_to_database()
