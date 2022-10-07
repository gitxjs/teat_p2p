
import app

class trustAPI():
    def __init__(self):
        self.trust_register_url=app.BASE_URL+'/trust/trust/register'

    def trust_register(self,session):
        response=session.post(self.trust_register_url)