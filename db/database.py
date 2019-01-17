class UsersDb(object):
    """
    A class used to represent the users list.

    Methods
    -------
    add_user(user)
        appends user to the users_list
    get_all_users
        returns a list with all users
    find_user_by_username(username)
        finds the user given their username
    check_user(username, password)
        checks for the user in the users_list
    """

    def __init__(self):
        """
        initialize the users list
        """
        self.users_list = []

    def add_user(self, user):
        """
        appends user to the users_list
        """
        self.users_list.append(user)

    def get_all_users(self):
        """
        returns a list with all users
        """
        return self.users_list

    def find_user_by_username(self, username):
        """
        finds the user given their username
        returns: user
        """
        for user in self.users_list:
            if user.username == username:
                return user
        return None

    def check_user(self, username, password):
        """
        finds the user given their username and password
        returns: user
        """
        for user in self.users_list:
            if username == user.username and password == user.password:
                return user
            return None


class RedflagsDb(object):
    """
    A class used to represent the redflags list.

    Methods
    -------
    add_redflag(redflag)
        appends a redflag to the redflag_list
    get_all_redflags
        returns a list with all redflags
    """

    def __init__(self):
        """
        initialize the redflags list
        """
        self.redflags_list = []

    def add_redflag(self, redflag):
        """
        appends a redflag to the redflags_list
        """
        self.redflags_list.append(redflag)

    def get_all_redflags(self):
        """
        returns a list with all redflags
        """
        return self.redflags_list
