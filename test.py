from endpoints.auth import credential, STORENAME, API_KEY, API_SECRET, ACCESS_TOKEN


class Test_Auth:
    def test_credentials(self):
        assert credential
        assert STORENAME
        assert API_KEY
        assert API_SECRET
        assert ACCESS_TOKEN
        
        
