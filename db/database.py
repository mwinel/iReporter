class UsersDb:

    def __init__(self):
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)

    def find_by_username(self, username):
        for user in self.users_list:
            if user.username == username:
                return user
        return None    