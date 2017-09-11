import requests

def get_token():
    resp = requests.get("https://instagram.com")
    csfrtoken = resp.cookies['csrftoken']
    return csfrtoken

if __name__ == "__main__":
    print get_token()

#hallo
