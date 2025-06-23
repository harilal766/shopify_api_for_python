from endpoints.auth import credential, STORENAME, API_KEY, API_SECRET, ACCESS_TOKEN
from endpoints.base import Base

class Test_Auth:
    def test_credentials(self):
        assert credential
        assert STORENAME
        assert API_KEY
        assert API_SECRET
        assert ACCESS_TOKEN
        
        
class Test_Base:
    def test_base_init(self):
        base_inst = Base()
        assert base_inst.storename
        assert base_inst.access_token
        assert base_inst.api_key
        assert base_inst.api_secret
        
    def test_creds_pattern(self):
        pass
    
    def test_make_request(self):
        pass
        
class Test_Orders:
    def test_unfulfilled_orders(self):
        pass
    
    def test_fulfilled_orders(self):
        pass
    
    def test_order_detail(self):
        pass
    
    


# Manual Test
from endpoints.order import Order

b = Base(); o = Order()


ord = o.get_orders(limit=20,fulfill=0)
#print(o.base_url)
print(ord)
