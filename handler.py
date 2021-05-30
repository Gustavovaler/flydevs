import json
import requests

def hello(event, context):
    body = requests.get('https://pokeapi.co/api/v2/pokemon')
    

    # body = {
    #     "message": "Este servidor de prueba!!",
        
    # }

    response = {"statusCode": 200, "body": body.json()}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
