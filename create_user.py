from anonbox import generate_email
import requests
import random

csrf = "B5YVdTtPdPvRiKC1sFNQyuVDSBBzsYgC"


def create_user():
    """
    This method creates a user with random username, password
    :return: username, password, cookies
    """
    email, mailbox, address, mailbox_name, date_hash = generate_email(True)

    password = "%s:%s:%s" % (mailbox_name, address, date_hash)
    username = "_%s_%s" % (address, date_hash)

    first_names = [
        "Max Botsen",
        "Botty Botbot",
        "Deine Butter",
        "Bots Lol",
        "Nope not suspicious"
    ]

    random.shuffle(first_names)

    first_name = first_names[0]

    data = {
        "email": email,
        "password": password,
        "username": username,
        "first_name": first_name,
    }

    headers = {
        "x-csrftoken": csrf,
        "referer": "https://www.instagram.com",
        #"x-instagram-ajax": "1",
    }

    cookies = {
        "csrftoken": csrf,
    }

    req = requests.post(  # Posting everything to www.instagram.com/accounts/web_create_ajax
        "https://www.instagram.com/accounts/web_create_ajax/",
        data=data,
        headers=headers,
        cookies=cookies
    )

    if req.status_code == 200:
        return req.text, username, password, mailbox
    else:
        return req.status_code, req.text
