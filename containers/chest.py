from typing import Set

from inspectable import Inspectable
from items import Tape, get_chest_combination


class Chest(Inspectable):
    __combination = []

    def __init__(self):
        super().__init__()
        self.name = "A chest"
        self.description = "A chest with a round pad lock on the outside."
        self.is_locked = True

    def inspect(self) -> Set:
        found_items = set()
        if self.is_locked:
            numbers = []
            print("You inspect the chest and pull on the lock on the outside but its locked. \n"
                  "The lock can spin left or right to enter a number of which there are 9.\n"
                  "To enter a number like 3 Left, enter: 3L")

            numbers.append(input("What is the first number you enter? ").upper())
            numbers.append(input("What is the second number you enter? ").upper())
            numbers.append(input("What is the third number you enter? ").upper())

            print("You entered " + str(numbers))
            if numbers == get_chest_combination():
                self.is_locked = False
                print("The lock opens and you recover a cassette tape from inside the box")
                found_items.add(Tape())

            else:
                print("You pull on the lock, but it is still locked.")

        else:
            print('There is nothing left in the box.')

        return found_items
