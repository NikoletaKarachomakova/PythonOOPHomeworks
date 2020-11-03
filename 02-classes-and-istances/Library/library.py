from Library.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user:User):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            del self.rented_books[user.username]

    def change_username(self, user_id: int, new_username: str):
        user_id_library = [user.user_id for user in self.user_records]
        if user_id in user_id_library:
            index = user_id_library.index(user_id)
            current_user = self.user_records[index]
            if current_user.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
            if current_user.username in self.rented_books:
                value = self.rented_books[current_user.username]
                del self.rented_books[current_user.username]
                self.rented_books[new_username] = value
            else:
                current_user.username = new_username

            return f"Username successfully changed to: {new_username} for userid: {user_id}"

        else:
            return f"There is no user with id = {user_id}!"
