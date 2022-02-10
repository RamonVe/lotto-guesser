# This class creates a future test object.
class FutureTestResults:
    def __init__(self, user, time, kp, bz, lottery_name, lottery_date, item_guesses, number_item_pair,
                 winning_numbers,
                 correct_guesses):
        self.user = user.user_details_list(),
        self.time = time
        self.kp = kp,
        self.bz = bz,
        self.lottery_name = lottery_name,
        self.lottery_date = lottery_date,
        self.item_guesses = item_guesses,
        self.number_item_pair = number_item_pair,
        self.winning_numbers = winning_numbers,
        self.correct_guesses = correct_guesses

    # Function returns the user associated to the future test as a list.
    def user(self):
        return self.user

    # Function returns the time associated to the future test.
    def time(self):
        return self.time

    # Function returns recorded Geomagnetic KP of the test at the time it was taken.
    def kp(self):
        return self.kp

    # Function returns recorded Geomagnetic BZ of the test at the time it was taken.
    def bz(self):
        return self.bz

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

    def winning_numbers(self):
        return self.winning_numbers

    def correct_guesses(self):
        return self.correct_guesses
