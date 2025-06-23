from endpoints.base import Base
import requests
class Order(Base):
    def __init__(self):
        super().__init__()
        self.base_url = f"{self.base_url}/orders.json"
    
    def get_orders(self,fulfill,limit=None):
        try:
            self.params.update({
                "limit" : limit if limit else 250
            })
        except Exception as e:
            pass
        else:
            response = requests.get(self.base_url,headers=self.headers,params=self.params)
            print(response.json())
        
