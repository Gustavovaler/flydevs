import json
import requests

def hello(event, context):
    try:
      limit = int(event['queryStringParameters']['limit'])
    except:
      limit = 100
    try:
      name = event['queryStringParameters']['name']
    except:
      name = 'pi'
    
    try:
      limit = event['queryStringParameters']['offset']
    except:
      offset = 0

    res  = requests.get('https://pokeapi.co/api/v2/pokemon?limit=2000')
    
    data = [data for data in res.json()['results'] if data['name'].startswith(name)]

    body = {"count": len(data), "results": data[offset:offset+limit]}

    return json.dumps(body)
