class UsersDb:

    def __init__(self):
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)     