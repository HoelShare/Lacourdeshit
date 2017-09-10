import requests
import time
import traceback
import simplejson

following = []


headers = {
    "Cookie": "",
    "X-CSRFToken": "",
    "X-Instagram-AJAX":"1",
    "Referer":"https://www.instagram.com/"
}

class not_following_err:
    pass

def follow(user, id, headers):
    url = "https://www.instagram.com/web/friendships/"+id+"/follow/"
    print url
    resp = requests.post(url, headers=headers)
    following.append(user)
    try:
        if resp.json()['result'] == "following":
            print "ok, followed:", user,id
        elif resp.json()['result']=="requested":
            print "ok requested:", user,id
        else:
            print resp.text
            raise not_following_err
    except KeyError:
        print "error occured: %s skipped"%user
    except simplejson.scanner.JSONDecodeError:
        print "json error:",
        if "Please wait a few minutes before you try again." in resp.text:
            print "Please wait a few minutes before you try again.", "sleeping for 120 secs"
            time.sleep(120)
            return False
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
