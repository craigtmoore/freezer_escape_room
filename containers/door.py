from typing import Set

from inspectable import Inspectable


class Door(Inspectable):

    def __init__(self):
        super().__init__()
        self.name = "door"
        self.description = "a door"

    def inspect(self) -> Set:
        print("You bang on the door and cry for help, but there is no answer.")
        print("You look all around the door but only see the button next to it")
        return set()
