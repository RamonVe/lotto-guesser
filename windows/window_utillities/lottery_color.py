def color(lottery):
    if lottery == 'Powerball':
        return 'red'
    elif lottery == 'Mega Millions':
        return 'gold'
    elif lottery == 'Lotto America':
        return 'yellow'
    elif lottery == 'Cash 4 Life':
        return 'green'
    else:
        return 'gold'


def text_color(lottery):
    lottery_color = color(lottery)
    if lottery_color == 'yellow':
        return 'black'
    elif lottery_color == 'gold':
        return 'black'
    else:
        return 'white'
