from random import shuffle
from typing import Set, List

from inspectable import Inspectable
from interactable import Interactable
from usable import Usable


class Flashlight(Usable, Inspectable, Interactable):

    def __init__(self):
        super().__init__()
        self.name = "flashlight"
        self.description_start = "You inspect the flashlight and click it on."
        self.description_end_no_batteries = "Nothing happens so you put it back."
        self.description = "A flashlight"
        self.has_batteries = False

    def inspect(self) -> Set:
        if self.has_batteries:
            print(self.description_start)
            print("A blue UV light shines from the flashlight. You click it off and add it to your inventory.")
        else:
            print(self.description_start + " " + self.description_end_no_batteries)

        return set()

    def can_pickup(self) -> bool:
        return self.has_batteries

    def interact(self, usable: Usable) -> List:
        if isinstance(usable, Batteries):
            print("You insert the batteries into the flashlight")
            self.has_batteries = True
            self.inspect()
            return [self]

        if isinstance(usable, Hammer):
            print("You worry you will break the flashlight so you don't smash it")

        elif isinstance(usable, TapePlayer):
            print("You consider playing the tape for the flashlight, but that's silly so you don't.")

        elif isinstance(usable, Tape):
            print("What am I thinking?! I can't put a tape in this!")

        return []


class Hammer(Usable):

    def __init__(self):
        super().__init__()
        self.name = "hammer"
        self.description = "A metal hammer with a rubber grip"


class Batteries(Usable):

    def __init__(self):
        super().__init__()
        self.name = "batteries"
        self.description = "A pair of very cold batteries."


class Tape(Usable):

    def __init__(self):
        super().__init__()
        self.name = "tape"
        self.description = "A tape that has a word CB scribbled on the side"


class TapePlayer(Usable, Inspectable, Interactable):

    def __init__(self):
        super().__init__()
        self.has_tape = False
        self.name = "tape player"
        self.description_start = "You inspect the tape player and click the play button."
        self.description_end_no_tape = "Nothing happens, looking closer you can see there is no cassette tape inside."
        self.description = "a tape player"

    def inspect(self) -> Set:
        if self.has_tape:
            print(self.description_start)

            combination = get_circuit_panel_combination()

            print("It begins to play:")
            print(f'  "The {combination[0]} bird sings sweetly')
            print(f'   in the {combination[1]} meadow')
            print(f'   full of {combination[2]} flowers')
            print(f'   as the {combination[3]} sun sets"')
        else:
            print(self.description_start + " " + self.description_end_no_tape)

        return set()

    def interact(self, usable: Usable) -> List:
        if isinstance(usable, Tape):
            print("You insert the tape into the player")
            self.has_tape = True
            self.inspect()

        elif isinstance(usable, Hammer):
            print("You worry you will break the tape player so you don't smash it")

        elif isinstance(usable, Flashlight):
            print("You shine the flash light on the tape player, but nothing stands out")

        elif isinstance(usable, Batteries):
            print("You open the battery compartment, but there are already batteries in the tape player so you put"
                  " them back in your pocket.")

        return []

    def can_pickup(self) -> bool:
        return self.has_tape


class Paper(Interactable, Inspectable):

    def __init__(self):
        super().__init__()
        self.name = "paper"
        self.description = "A blank piece of paper"

    def inspect(self) -> Set:
        print("You look at the paper closely, but appears blank.")
        return set()

    def interact(self, usable: Usable) -> List:

        combination = ""
        for combo in get_chest_combination():
            combination += combo

        if isinstance(usable, Flashlight):
            print(f'You shine the {usable.name} on the paper and this text appears \n\n  {combination}')

        else:
            print(f'You hold the {usable.name} near the paper, but nothing happens (what did you expect?!)')

        return []


__chest_combination = []


def get_chest_combination() -> List[str]:
    if __chest_combination:
        return __chest_combination

    letters = ['R', 'L', 'R']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    for i in range(0, 3):
        number = numbers[i]
        letter = letters[i]
        __chest_combination.append(f"{number}{letter}")
    return __chest_combination


__circuit_breaker_combination = []


def get_circuit_panel_combination() -> List[str]:
    if __circuit_breaker_combination:
        return __circuit_breaker_combination

    words = ['blue', 'red', 'green', 'yellow']
    shuffle(words)
    __circuit_breaker_combination.extend(words)

    return __circuit_breaker_combination
