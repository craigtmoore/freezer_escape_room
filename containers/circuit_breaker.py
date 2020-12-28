from typing import Set

from inspectable import Inspectable

COMBINATION = 'BGYR'


class CircuitBreakerPanel(Inspectable):

    def __init__(self):
        super().__init__()
        self.name = 'circuit breaker'
        self.description = "A circuit breaker panel"
        self.is_powered = False

    def inspect(self) -> Set:
        print('You look at the circuit breaker panel and see a panel with 4 colored switches of '
              'Blue, Red, Yellow, and Green')
        print('To enter the colors for example for Blue, Red, Yellow, and Green, then you would enter'
              ' \'BRYG\'')
        colors = input('Enter the order of the switches you wish to enter: ')
        colors_entered = []
        for color in colors:
            if color.upper() == 'B':
                colors_entered.append('blue')
            elif color.upper() == 'R':
                colors_entered.append('red')
            elif color.upper() == 'G':
                colors_entered.append('green')
            elif color.upper() == 'Y':
                colors_entered.append('yellow')

        print(f'You entered {colors_entered}')

        if colors == COMBINATION:
            print('You see lights on the circuit breaker panel turn on as power is restored.')
            self.is_powered = True
        else:
            print('Nothing happened, and the lights on the panel are still off.')

        return set()
