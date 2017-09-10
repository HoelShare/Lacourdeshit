import requests
import headers
import follow

headers = headers.headers

uids=[["5985933082","dhsduhui"]]

for uid in uids:
    resp = requests.get("https://www.instagram.com/graphql/query/?query_id=17874545323001329&variables={\"id\":"+uid[0]+",\"first\":4000}", headers=headers).json()
    for user in resp['data']['user']['edge_follow']['edges']:
        usern = user['node']['username']
        uid = user['node']['id']
        uids.append([uid, usern])
        s = follow.follow(usern, uid, headers)
        
