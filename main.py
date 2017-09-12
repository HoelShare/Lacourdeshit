import requests
import headers
import follow
import time
import create_user
import ibcao_login

headers = headers.headers

uids=[["5985933082","dhsduhui"]]

class User:
    def __init__(self):
        self.csrf = ibcao_login.get_token()
        self.resp, self.username, self.password, self.mailbox, self.cookies = create_user.create_user(self.csrf)
    def get_creds(self):
            print self.resp, self.username, self.password, self.mailbox, self.cookies


def checkfollow(username):
    resp = requests.get("https://www.instagram.com/"+username+"/?__a=1", headers=headers)
    if "Please wait a few minutes before you try again" in resp.text:
        print "Please wait a few minutes before you try again.","sleeping now for 2mins"
        time.sleep(120)
    else:
        return resp.json()['user']['followed_by_viewer']

def nachbarschafts():
    for uid in uids:
        resp = requests.get("https://www.instagram.com/graphql/query/?query_id=17874545323001329&variables={\"id\":"+uid[0]+",\"first\":4000}", headers=headers).json()
        for user in resp['data']['user']['edge_follow']['edges']:
            usern = user['node']['username']
            uid = user['node']['id']
            uids.append([uid, usern])
            if checkfollow(usern) == False:
                s = follow.follow(usern, uid, headers)
                print "-"*60
                print "NOOT NOOT: ICH FOLGE NOCH NICHT:", usern
                print "-"*60
            else:
                print "ich folge schon:", usern
cuser = User()
cuser.get_creds()
