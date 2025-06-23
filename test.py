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