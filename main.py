import create_user
import follow
import requests
import headers

headers = headers.headers

users = []
class no_cookie:
    pass


class User:
        def __init__(self, created=False, headers=None):
            self.headers = headers
            self.counter = 0
            self.created = created
            if self.created == False:
                self.i, self.username, self.password, self.mailbox = create_user.create_user()
        def follow(self, uid, uname):
            self.uid = uid
            self.uname = uname
            follow.follow(self.uname, self.uid, self.headers)
            self.counter += 1
        def get_headers(self):
            if self.headers==None:
                raise no_cookie
            return self.headers
        def get_counter(self):
            return self.counter
        def get_credentials(self):
            if self.created == False:
                return self.username, self.password, self.mailbox
            else:
                return None

userid = "6860189"

def getfirst(fuid, userob):
    resp = requests.get("https://www.instagram.com/graphql/query/?query_id=17851374694183129&variables={\"id\":" + fuid + ",\"first\":1000}",headers=userob.get_headers()).json()
    uname = resp['data']['user']['edge_followed_by']['edges'][1]['node']['username']
    uid = resp['data']['user']['edge_followed_by']['edges'][1]['node']['id']
    userob.follow(uname, uid)
    print "counter:",userob.get_counter()
    if userob.get_counter() > 100:
        userob = User()
        users.append(fuser)
        print "created new user bc old one reached limit"
        print fusers

fuser = User(True, headers)

users.append(fuser)

getfirst(userid, fuser)

for us in users:
    print us.get_credentials()
