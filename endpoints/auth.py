import json


with open('api_credentials.json','r') as json_file:
    api_creds = json.load(json_file)
    
credential = tuple(api_creds.keys())[0]    
    

ACCESS_TOKEN = credential["access_token"]
STORENAME = credential["storename"]
API_KEY = credential["api_key"]
API_SECRET = credential["api_secret"]