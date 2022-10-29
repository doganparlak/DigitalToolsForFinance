

Original file is located at
    https://colab.research.google.com/drive/1jW56HVNfzHDSpLG2vsEN0BCTTIY63yYM
"""

## Import all necessary libraries
from matplotlib import pyplot
import os
import requests
!pip install fredapi
import fredapi
from fredapi import Fred


# Source https://lvngd.com/blog/fred-api-python/
individual_fred_key = "abc123" # fake api key
PRIVATE_API_KEY="83561680681e19c53a6ad7a3d199f7ad"
api_key = os.environ.get("PRIVATE_API_KEY")



# Question 2
ROOT_URL = "https://api.stlouisfed.org"

# Question 3
ENDPOINT = "/fred/series/observations"

# Question 4
params = {
    'api_key': PRIVATE_API_KEY,
    'series_id': 'UNRATE',
    'file_type': 'json', # or xml
    'observation_start': '2020-01-01'
}

# Send a request to the Fred server & receive a response
resp = requests.get(f"{ROOT_URL}{ENDPOINT}", params = params)

# resp == 400 (failed) with the fake api key, but resp == 200 with a valid key
print(resp) 

# Alternative solution: use wrapper by mortdata
# Source https://github.com/mortada/fredapi, https://pypi.org/project/fredapi/
fred = Fred(api_key = PRIVATE_API_KEY)
unRateSeries = fred.get_series('UNRATE', '2020-01-01') # returns pandas Series

# Create a timeseries plot
unRateSeries.plot()
pyplot.show()

# Density plot
unRateSeries.plot(kind='kde')
pyplot.show()
