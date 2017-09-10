import requests
import time
import traceback

following = []


headers = {
    "Cookie": "",
    "X-CSRFToken": "",
    "X-Instagram-AJAX":"1",
    "Referer":"https://www.instagram.com/"
}
def follow(user, id, headers):
    url = "https://www.instagram.com/web/friendships/"+id+"/follow/"
    resp = requests.post(url, headers=headers)
    following.append(user)
    print resp.text
    print "ok, followed:", user,id

def getfollows():
    resp = requests.get("https://www.instagram.com/graphql/query/?query_id=17874545323001329&variables={\"id\":\"5985933082\",\"first\":1000}", headers=headers).json()
    for i in  resp['data']['user']['edge_follow']['edges']:
        following.append(i['node']['username'])

def foolow(userid):
    resp = requests.get(
        "https://www.instagram.com/graphql/query/?query_id=17851374694183129&variables={\"id\":" + userid + ",\"first\":1000}",
        headers=headers).json()
    try:
        for i in resp['data']['user']['edge_followed_by']['edges']:
            user = i['node']['username']
            userid = i['node']['id']
            if "lacourdeschit" not in user and user not in following:
                follow(user, userid)
                foolow(userid)
            else:
                print "entweder folge ich mir selbst oder jmd. dem ich schon folge"
    except Exception, e:
        print e, "test"
        traceback.print_exc()
