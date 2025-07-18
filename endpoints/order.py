from endpoints.base import Base
import requests
from pprint import pprint
class Order(Base):
    def __init__(self):
        super().__init__()
        self.base_url = f"{self.base_url}/orders.json"
    
    def get_orders(self,fulfill,graphql: bool = None,limit: int = None,):
        response = None
        try:
            self.params.update({
                "limit" : limit if limit else 250
            })
        except Exception as e:
            pass
        else:
            if graphql == True:
                query = """
                query {
                    orders(first:5, sortKey: CREATED_AT, reverse: true, query:"fulfillment_status:unfulfilled") {
                        edges {
                            node {
                                name
                                phone
                            }
                        }
                    }
                }
                """
                response = requests.post(self.graphql_url,headers=self.headers, json={"query" : query})
            else:
                response = requests.get(self.base_url,headers=self.headers,params=self.params)
                
                
            pprint(response.json())
        
