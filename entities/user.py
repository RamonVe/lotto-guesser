class User:
    def __init__(self, first_name, last_name, age, location, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.username = username
        self.password = password

    def first_name(self):
        return self.first_name

    def user_details_list(self):
        user_details_list = [self.first_name, self.username, self.location]
        return user_details_list
