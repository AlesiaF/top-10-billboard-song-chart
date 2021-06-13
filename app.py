import requests
import config
import api_data

response = requests.request('GET', config.api_url, headers=api_data.headers, params=api_data.querystring)
data = response.json()

print('Billboard Top 10 Hits - ' + config.api_date)

for i in range(1, 11):
    i = str(i)
    print('Rank: ' + data['content'][i]['rank'])
    print('Artist: ' + data['content'][i]['artist'])
    print('Title: ' + data['content'][i]['title'])
    print('Weeks On Chart: ' + data['content'][i]['weeks on chart'])
    print('')
