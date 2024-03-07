import requests
symbol = 'LTCBTC'
api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
response = requests.get(api_url, headers={'X-Api-Key': 'ug37mn6QegzJ8J3q0oBz3A==vESsyPdBHLLNWS6p'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)