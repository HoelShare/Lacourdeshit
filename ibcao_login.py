import requests

def get_token():
    resp = requests.get("https://instagram.com")
    csfrtoken = resp.cookies['csrftoken']
    print csfrtoken
if __name__ == "__main__":
    get_token()
