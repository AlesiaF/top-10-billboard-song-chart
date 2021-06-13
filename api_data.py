import config

querystring = {
    "date":config.api_date,
    "range":"1-10"
}

headers = {
    'x-rapidapi-key': config.api_key,
    'x-rapidapi-host': config.api_path
}