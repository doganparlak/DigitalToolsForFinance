#upstream.py
import datetime
import quandl
import pandas as pd
import os
import pyarrow.feather as feather
import json
import requests

from connect import DATAPATH

def put_data():
    """ Store the data into the database"""

    data ="upstream test"

    filename = DATAPATH + "commodity_prices_august_2021.csv"

    data.to_csv(filename)

put_data()
