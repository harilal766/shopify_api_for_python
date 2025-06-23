from endpoints.auth import ACCESS_TOKEN,API_KEY,API_SECRET,STORENAME

class Base:
    def __init__(self):
        self.storename = STORENAME
        self.access_token = ACCESS_TOKEN
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.version = "2025-04"
        self.endpoint = None
        
        if self.storename and self.version:
            self.base_url = f"https://{self.storename}.myshopify.com/admin/api/{self.version}"
            
            self.headers = {
                "Content-Type" : "application/json",
                "X-Shopify-Access-Token" : self.access_token
            }
            
            self.params = {}
            
    def make_request(self):
        try:
            pass
        except:
            pass
        else:
            pass
            