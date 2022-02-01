import random


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


def past_or_present():
    random_past_present = random.randint(1, 100)

    if random_past_present <= 70:
        return '2021'
    else:
        return '2022'
