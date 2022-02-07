import random


# This function returns a random 2021 or early 2022 lottery results depending on the lottery name.
def random_lottery_details(selected_lottery):
    if selected_lottery == 'Powerball':
        if past_or_present() == '2021':
            power_ball_twenty_one = open('past_lotteries/tn-powerball-2021.txt', 'r').readlines()
            random_details = random.choice(power_ball_twenty_one)
            return random_details
        else:
            power_ball_twenty_two = open('past_lotteries/tn-powerball-2022.txt', 'r').readlines()
            random_details = random.choice(power_ball_twenty_two)
            return random_details
    elif selected_lottery == 'Mega Millions':
        if past_or_present() == '2021':
            mega_millions_twenty_one = open('past_lotteries/tn-mega-millions-2021.txt', 'r').readlines()
            random_details = random.choice(mega_millions_twenty_one)
            return random_details
        else:
            mega_millions_twenty_two = open('past_lotteries/tn-mega-millions-2022.txt', 'r').readlines()
            random_details = random.choice(mega_millions_twenty_two)
            return random_details
    elif selected_lottery == 'Lotto America':
        if past_or_present() == '2021':
            lotto_america_twenty_one = open('past_lotteries/tn-lotto-america-2021.txt', 'r').readlines()
            random_details = random.choice(lotto_america_twenty_one)
            return random_details
        else:
            lotto_america_twenty_two = open('past_lotteries/tn-lotto-america-2022.txt', 'r').readlines()
            random_details = random.choice(lotto_america_twenty_two)
            return random_details
    elif selected_lottery == 'Cash 4 Life':
        if past_or_present() == '2021':
            cash_four_life_twenty_one = open('past_lotteries/tn-cash4life-2021.txt', 'r').readlines()
            random_details = random.choice(cash_four_life_twenty_one)
            return random_details
        else:
            cash_four_life_twenty_two = open('past_lotteries/tn-cash4life-2022.txt', 'r').readlines()
            random_details = random.choice(cash_four_life_twenty_two)
            return random_details
    else:
        if past_or_present() == '2021':
            tn_cash_twenty_one = open('past_lotteries/tn-tennessee-cash-2021.txt', 'r').readlines()
            random_details = random.choice(tn_cash_twenty_one)
            return random_details
        else:
            tn_cash_twenty_two = open('past_lotteries/tn-tennessee-cash-2022.txt', 'r').readlines()
            random_details = random.choice(tn_cash_twenty_two)
            return random_details


# This function randomly picks either 2021 or 2022 for use in the random lottery details function.
# Currently, there is a 75% chance for 2021 to be returned since the 2022 lotteries don't have as
# many results as the 2021 lotteries.
def past_or_present():
    random_past_present = random.randint(1, 100)

    if random_past_present <= 75:
        return '2021'
    else:
        return '2022'
