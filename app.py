import requests
import config
import api_data

response = requests.request('GET', config.api_url, headers=api_data.headers, params=api_data.querystring)
data = response.json()

