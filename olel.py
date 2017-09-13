import instagram_usermanager
import create_user
import ibcao_login
from debug import info, warning, error
import runtime  # With importing this module a counter "starts" and counts the
                # second, the program runs

name = "olel"

manager = instagram_usermanager.InstagramUserManager("db")

# Creating a csrf token with this module to
# spoof instagrams browser detection mechanism
csrf = ibcao_login.get_token()
info("got csrf token (%s)" % csrf, runtime, name)

# Creating a new user with email and other important stuff.
ret = create_user.create_user(csrf)
if len(ret) == 6:  # create_user returns 6 values if everything is ok, else 2
    js, username, password, mail, mailbox, cookies = ret

    if js["account_created"] and js["status"] == "ok": # Checking if everything worked
        uid = js["user_id"]
        # creating a new user object to store in database
        user = instagram_usermanager.InstagramUser(username, uid, mail, password, csrf, cookies)
        manager.add_user(user)
        manager.gen_db()
        manager.write_db()
        info("registered user: %s" % user, runtime, name)
    else:
        error("Couldn't register user!; Received:\n\t%s" % (js), runtime, name)

else:
    code, text = ret
    error("Received error code: %d;\n\t%s" % (code, text), runtime, name)
