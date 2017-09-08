import requests
import time

headers = {
    "Cookie": "",
    "X-CSRFToken": "",
    "X-Instagram-AJAX":"1",
    "Referer":"https://www.instagram.com/"
}
def follow(user, id):
    headers = {
        "Cookie": "",
        "X-CSRFToken": "",
        "X-Instagram-AJAX": "1",
        "Referer": "https://www.instagram.com/"+user+"/"
    }
    requests.post("https://www.instagram.com/web/friendships/"+id+"/follow/", headers=headers)

def getfollows():
    start = input("start?")
    counter = 0
    resp = requests.get("https://www.instagram.com/graphql/query/?query_id=17851374694183129&variables={\"id\":\"6860189\",\"first\":1000}", headers=headers).json()
    for i in  resp['data']['user']['edge_followed_by']['edges']:
        counter+=1
        user = i['node']['username']
        id = i['node']['id']
        follow(user,id)
        print "followed:", user, "follower:",counter, "start:", start
        time.sleep(30

getfollows()
