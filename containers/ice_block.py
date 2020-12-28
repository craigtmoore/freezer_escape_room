from typing import Set, List

from inspectable import Inspectable
from interactable import Interactable
from items import Batteries, Hammer
from usable import Usable


class IceBlock(Inspectable, Interactable):

    def __init__(self):
        super().__init__()
        self.name = 'ice block'
        self.description = 'A large block of ice'
        self.is_broken = False

    def inspect(self) -> Set:
        if self.is_broken:
            print('Pieces of ice litter the floor where you shattered it earlier.')
        else:
            print('You look closely at the ice and see a pair of batteries are frozen inside.')
            print('You attempt to smash the ice on the floor to get them out, but it is too ')
            print('solid to break that way, you\'ll need something to smash it')

        return set()

    def interact(self, usable: Usable) -> List:
        found_items = []

        if self.is_broken:
            print(f'You attempt to use the {usable.name} on pieces of ice and start to wonder if you\'re going crazy')
        elif isinstance(usable, Hammer):
            print('You smash the ice with the hammer until it shatters and the batteries fall to the floor.')
            print('You collect the batteries and put them in your pocket.')
            found_items.append(Batteries())
        else:
            print(f'You attempt to use the {usable.name} on the block of ice, but it does not look like it will work '
                  f'so you stop.')

        return found_items
