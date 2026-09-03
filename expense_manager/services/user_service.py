from models import User


class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, name, username):
        if self.find_by_username(username):
            raise ValueError("Username already exists.")

        user_id = len(self.users) + 1
        user = User(user_id, name, username)
        self.users.append(user)
        return user

    def find_by_username(self, username):
        return next(
            (user for user in self.users if user.username.lower() == username.lower()),
            None,
        )

    def get_user(self, user_id):
        return next((user for user in self.users if user.user_id == user_id), None)
