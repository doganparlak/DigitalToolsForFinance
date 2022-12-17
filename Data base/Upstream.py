#upstream.py
import datetime
import quandl
import pandas as pd
import os
import pyarrow.feather as feather
import json
import requests

from connect import DATAPATH

quandl.ApiConfig.api_key = os.environ.get("QUANDL_API_KEY")

def put_fx_data():
    """ fx and dates should be entered """
    
  data = quandl.get("fx", start_date="", end_date="")

  filename = DATAPATH + "fx.ftr"

  data.to_feather(filename)
