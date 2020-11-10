
class User():
    username = "admin"
    email = "admin@example.com"
    password = "admin"
    userStatus = "Business"

    def __init__(self, un, e, p, us):
        self.username = un
        self.email = e
        self.password = p
        self.userStatus = us

    def display(self, username, email, password, userStatus):
        print(username + email + password + userStatus)