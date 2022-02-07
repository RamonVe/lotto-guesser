# This class creates a future test object.
class FutureTest:
    def __init__(self, user, time, lottery_name, lottery_date, item_guesses, number_item_pair):
        self.user = user.user_details_list(),
        self.time = time
        self.lottery_name = lottery_name,
        self.lottery_date = lottery_date,
        self.item_guesses = item_guesses,
        self.number_item_pair = number_item_pair

    # Function returns the user associated to the future test as a list.
    def user(self):
        return self.user

    # Function returns the time associated to the future test.
    def time(self):
        return self.time

    # Function returns the lottery name associated to the future test.
    def lottery_name(self):
        return self.lottery_name

    # Function returns the lottery date associated to the future test.
    def lottery_date(self):
        return self.lottery_date

    # Function returns the item guesses associated to the future test.
    def item_guesses(self):
        return self.item_guesses

    # Function returns the random number item pair generated associated to the future test.
    def number_item_pair(self):
        return self.number_item_pair
