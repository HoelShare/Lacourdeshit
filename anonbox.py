import requests

def generate_email(verbose=False):
    req = requests.get("https://anonbox.net/en")

    if req.status_code == 200:  # HTTP OK
        lines = req.text.split("\n")
        address = mailbox_name = date_hash = ""
        for line in lines:
            if "<dd><p>" in line and "'display: none' class=foobar" in line:
                address = line.split("<dd><p>")[1].split("<span")[0]
                date_hash = line.split("</span>@")[1].split("<span>")[0]
            if "<dd><p><a href=" in line and "https://anonbox.net/" + date_hash in line:
                mailbox_name = line.split(date_hash + "/")[1].split("\">")[0]
        email = "%s@%s.anonbox.net" % (address, date_hash)
        mailbox = "https://anonbox.net/%s/%s" % (date_hash, mailbox_name)

        if not verbose:
            return email, mailbox
        else:
            return email, mailbox, address, mailbox_name, date_hash

if __name__ == "__main__":
    print generate_email()
