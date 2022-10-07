import app

class approveAPI():
    def __init__(self):
        self.approve_url=app.BASE_URL+"/member"

    def approve(self,session,realname,cardid):
        data={'realname':realname,'cardid':cardid}
        response=session.post(self.approve_url,data=data,files={'x':'y'})
        return response