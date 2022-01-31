import random


class PowerBall:
    def __init__(self, ball_one, ball_two, ball_three, ball_four, ball_five, ball_six):
        self.ball_one = ball_one
        self.ball_two = ball_two
        self.ball_three = ball_three
        self.ball_four = ball_four
        self.ball_five = ball_five
        self.ball_six = ball_six

    def ball_one(self):
        return self.ball_one

    def ball_two(self):
        return self.ball_two

    def ball_three(self):
        return self.ball_three

    def ball_four(self):
        return self.ball_four

    def ball_five(self):
        return self.ball_five

    def ball_six(self):
        return self.ball_six


def white_ball_number():
    number = random.randint(1, 69)
    return number


def red_ball_number():
    number = random.randint(1, 26)
    return number

