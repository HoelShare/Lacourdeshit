import time
import cPickle
import os
import base64
import json
import time

NONE_DIRECOTRY = 0
NEW_DIRECTORY = 1
VALID_DIRECTORY = 2
INVALID_DIRECTORY = 3

FILE_EXTENSION = "iua"  # Instagram User Account

class InstagramUserManager(object):

    def __init__(self, directory):
        self.directory = directory

        self.db = {}
        self.users = []

        self.directory_state = self.validity_check(directory)
        if self.directory_state == NONE_DIRECOTRY:
            os.mkdir(self.directory)
            self.directory_state = NEW_DIRECTORY

        if self.directory_state == NEW_DIRECTORY:
            with open(self.directory + "/db.json", "wa") as target:
                target.write(json.dumps({
                    "users": [],
                    "created": 0
                }))
            self.directory_state = VALID_DIRECTORY

        if self.directory_state == VALID_DIRECTORY:
            with open(self.directory + "/db.json", 'r') as target:
                self.db = json.loads(target.read())

        if self.directory_state == INVALID_DIRECTORY:
            raise Exception("Invalid directory check twice and try again")

        for user in self.db["users"]:
            self.users.append(self.decode_user(user))

    def add_user(self, user):
        if not user in self.users:
            self.users.append(user)
            return True
        else:
            return False

    def gen_db(self):
        tmp = {
            "users": list(map(lambda x: x.encode(), self.users)),
            "created": int(time.time())
        }
        print tmp
        self.db = tmp


    def write_db(self):
        with open(self.directory + "/db.json", "wa") as target:
            target.write(json.dumps(self.db))

    def validity_check(self, directory):
        """
        This method checks a given directory for a database file
        """
        try:
            dlist = os.listdir(directory)
        except OSError:
            return NONE_DIRECOTRY
        if len(dlist) == 0:
            return NEW_DIRECTORY
        else:
            if "db.json" in dlist:
                return VALID_DIRECTORY
            else:
                return INVALID_DIRECTORY

    def get_db_users(self):
        """
        This method will read self.directory/db.json for all user names
        """
        with open(self.directory + "/db.json") as target:
            json_obj = json.loads(target.read())
        return json_obj["users"]

    @staticmethod
    def encode_user(user_object):
        return base64.b64encode(cPickle.dumps(user_object))

    @staticmethod
    def decode_user(string):
        return cPickle.loads(base64.b64decode(string))

class InstagramFollower(object):

    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def __str__(self):
        return "%s with uid %s" % (self.username, self.user_id)

class InstagramUser(object):

    def __init__(self, username, user_id, mail, password, csrf, cookies):
        self.username = username
        self.mail = mail
        self.password = password
        self.user_id = user_id


        self.csrf = csrf
        self.cookies = cookies

        self.is_blocked = False
        self.estimated_blocked_until = time.time()

        self.following = []

    def add_follower(self, follower):
        if not follower in self.following:
            self.following.append(follower)
            return True
        else:
            return False

    def __str__(self):
        return "%s with %d cookies" % (self.username, len(self.cookies))

    def encode(self):
        return InstagramUserManager.encode_user(self)

if __name__ == "__main__":
    user = InstagramUser("test", "aaaaaaa", "abc", "cbaa", "dklfnwner23nti2", {'NOPE': 1, "BLA": "N"})
    user2= InstagramUser("test2", "bbbbbbbb", "cba", "aabc", "ifnlksnfln3ln2", {"meh": "dope", "bla": 10})
    manager = InstagramUserManager("test")
    
