def login_user(username, password):
    """
    This method tries to login a user, if it has success, it will return a json
    with information about username availability and password availability and
    a json with all cookies, if password and username were correct, these cookies
    can be used to make more interaction with the API.
    :param username: The username of the instagram account
    :param password: The password of the instagram account
    :return:
    """
    data = {  # Defining http post data
        "username": username,
        "password": password
    }

    headers = {  # Defining necessary headers
        "x-csrftoken": csrf,
        "referer": "https://www.instagram.com/",

    }

    cookies = {  # Defining necessary cookie(s)
        "csrftoken": csrf,
    }

    req = requests.post(  # Posting everything to www.instagram.com/accounts/login/ajax/
        "https://www.instagram.com/accounts/login/ajax/",
        data=data,
        headers=headers,
        cookies=cookies
    )

    if req.status_code == 200:  # Checking if the request got a 200 ("ok")
        js = json.loads(req.text)
        new = {  # Creating a new, more plausible json
            "valid_username": js["user"],
            "valid_password": js["authenticated"]
        }
        if js["status"] == "ok":  # checking status in old json
            cookies = {}
            for cookie in req.cookies:
                cookies.update({cookie.name: cookie.value})
            return new, cookies
        else:
            return False
    else:
        print req.text
        return False
