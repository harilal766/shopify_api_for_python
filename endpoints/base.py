from auth import ACCESS_TOKEN,API_KEY,API_SECRET,STORENAME

class Base:
    def __init__(self):
        self.storename = STORENAME
        self.access_token = ACCESS_TOKEN
        self.api_key = API_KEY
        self.api_secret = ACCESS_TOKEN 